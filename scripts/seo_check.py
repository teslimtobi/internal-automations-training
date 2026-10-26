#!/usr/bin/env python3
"""Check an Appnable blog .docx against the Appnable Blog Writing Guidelines.

Usage:
  python seo_check.py blog.docx --keyword "Copilot readiness assessment" \
      [--supporting "Copilot data security" "Microsoft 365 consultancy"] \
      [--chunks 1000 --outdir parts/]

Expected document layout (as produced by the seo-article-writer skill):
  header lines (Primary keyword:, Supporting keywords:, URL slug:, Meta description:, ...)
  Heading 1 title
  intro paragraphs
  Heading 2 body sections (Heading 3 sub-points)
  Heading 2 "Final thoughts" / "Conclusion"
  Heading 2 "Read also" (optional block)
  Heading 2 "FAQs" with Heading 3 questions
  Heading 2 "Pre-publish checklist" (ignored by the checks)

Results: OK = passes, FIX = fails a checklist rule, WARN = check by hand, INFO = for reference.
"""
import argparse, math, os, re, sys
from docx import Document
from docx.oxml.ns import qn

N_IMAGES = 0
READ_RE = re.compile(r'^\s*(also read|read also)\s*:', re.I)
CONCL_RE = re.compile(r'final thoughts|conclusion|in summary|wrapping up|next steps|^ready to', re.I)
FAQ_RE = re.compile(r'\bfaqs?\b|frequently asked', re.I)
READ_H_RE = re.compile(r'^\s*(read also|also read|related (articles|blogs|reading))\s*$', re.I)
CHECK_RE = re.compile(r'pre-publish checklist', re.I)
REF_RE = re.compile(r'^\s*(references|sources|bibliography)\s*$', re.I)
OWN_DOMAINS = ('appnable.com', 'kokoodi.com')
CTA_RE = re.compile(r'\b(book|download|contact|get in touch|talk to|speak to|schedule|request)\b', re.I)

US_SPELLINGS = {
    r'\b(organi|optimi|reali|recogni|priori|standardi|digiti|authori|customi|minimi|maximi|summari|utili|categori|emphasi|centrali|moderni|personali|visuali|monetis)z(e|es|ed|ing|ation|ations)\b': 'use -ise/-isation',
    r'\banalyz(e|es|ed|ing)\b': 'analyse', r'\bcolor(s|ed|ful)?\b': 'colour', r'\bcenter(s|ed)?\b': 'centre',
    r'\bbehavior(s|al)?\b': 'behaviour', r'\bfavor(ite|s|ed)?\b': 'favour', r'\blabor\b': 'labour',
    r'\bprogram(s)?\b(?! code)': 'programme (unless computer program)', r'\bcatalog(s)?\b': 'catalogue',
    r'\bdefense\b': 'defence', r'\boffense\b': 'offence', r'\bjudgment\b': 'judgement',
    r'\benroll(s|ment)?\b': 'enrol/enrolment', r'\btraveling\b': 'travelling', r'\bmodeling\b': 'modelling',
    r'\bcanceled\b': 'cancelled', r'\blicense\b(?= (fee|holder|cost|agreement|key))': 'licence (noun)',
    r'\bcheck(s)? (payment|book)\b': 'cheque', r'\bfulfill\b': 'fulfil',
}
BANNED = ['delve', 'leverage', 'robust', 'testament', 'crucial', 'game-changer', 'game changer', 'beacon', 'tapestry',
          'it is important to note', "it's important to note", "in today's fast-paced world", 'fast-paced world', 'at its core']
IMAGE_DOMAINS = ('unsplash.com', 'pexels.com', 'pixabay.com', 'undraw.co', 'manypixels.co', 'streamlinehq.com')
OWN_NAMES = re.compile(r'\b(appnable|kokoodi|stgatherly)\b', re.I)
FILLER = ('furthermore', 'moreover', 'additionally')
CLICHES = ["in today's fast-paced", 'fast-paced world', 'unlock the power', 'unlock the potential', 'game-changer',
           'game changer', 'seamless', 'seamlessly', 'leverage', 'delve', 'navigate the landscape', 'ever-evolving',
           'revolutionise', 'revolutionize', 'cutting-edge', 'in conclusion', "it's important to note", 'harness the power',
           'supercharge', 'elevate your', 'in the realm of', 'a testament to', 'look no further', 'treasure trove',
           'paradigm shift', 'synergy', 'robust solution', 'take it to the next level', 'in this day and age']
TRANSITIONS = ['also', 'however', 'in addition', 'additionally', 'as a result', 'for example', 'for instance', 'that said',
               'meanwhile', 'similarly', 'in practice', 'finally', 'furthermore', 'moreover', 'instead', 'likewise',
               'first', 'firstly', 'second', 'secondly', 'next', 'then', 'in short', 'as well', 'by contrast', 'in fact',
               'because of this', 'this means', 'on top of this', 'beyond this', 'with this in mind', 'to start',
               'better still', 'even so', 'equally', 'in turn', 'at the same time', 'once', 'after', 'before', 'today',
               'overall', 'ultimately', 'otherwise', 'besides', 'consequently', 'therefore', 'so', 'yet', 'still']
ACRONYM_OK = {'UK', 'US', 'EU', 'OK', 'FAQ', 'FAQS', 'URL', 'I', 'A'}


def heading_level(p):
    try:
        name = (p.style.name if p.style is not None else '') or ''
    except Exception:
        name = ''
    if not name and p._p.pPr is not None and p._p.pPr.pStyle is not None:
        name = p._p.pPr.pStyle.val or ''
    m = re.search(r'heading\s*(\d)', name, re.I)
    if m:
        return int(m.group(1))
    return 1 if name.lower() == 'title' else 0


def links_of(p, rels):
    out = []
    for h in p._p.iter(qn('w:hyperlink')):
        rid = h.get(qn('r:id'))
        url = rels[rid].target_ref if rid and rid in rels else ''
        text = ''.join(t.text or '' for t in h.iter(qn('w:t')))
        out.append((text, url))
    return out


def words(t):
    return len(re.findall(r"[A-Za-z0-9’'%£$€.,:/-]+", t))


def count(text, phrase):
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(phrase) + r'(?![A-Za-z])', text, flags=re.I))


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def load(path):
    doc = Document(path)
    rels = doc.part.rels
    global N_IMAGES
    N_IMAGES = len(doc.element.body.findall('.//' + qn('w:drawing')))
    header, paras, started = {}, [], False
    for p in doc.paragraphs:
        text = p.text.strip()
        lvl = heading_level(p)
        if not started:
            if lvl == 1:
                started = True
            else:
                m = re.match(r'^\s*([A-Za-z ]+?)\s*:\s*(.+)$', text)
                if m:
                    header[m.group(1).strip().lower()] = m.group(2).strip()
                continue
        if lvl and CHECK_RE.search(text):
            break
        if text:
            paras.append({'text': text, 'level': lvl, 'links': links_of(p, rels)})
    return header, paras


def sections(paras):
    """Split into title, intro, body H2 sections, conclusion, read-also block, faqs, references."""
    out = {'title': paras[0], 'intro': [], 'body': [], 'conclusion': [], 'readalso': [], 'faq': [], 'refs': []}
    cur, kind = None, 'intro'
    for p in paras[1:]:
        if p['level'] == 2:
            t = p['text']
            if REF_RE.match(t):
                kind = 'refs'
            elif READ_H_RE.match(t):
                kind = 'readalso'
            elif FAQ_RE.search(t):
                kind = 'faq'
            elif CONCL_RE.search(t):
                kind = 'conclusion'
            else:
                kind = 'body'
                cur = {'heading': p, 'paras': []}
                out['body'].append(cur)
            out.setdefault(kind + '_heading', p)
            continue
        if kind == 'body':
            cur['paras'].append(p)
        else:
            out[kind].append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('--keyword', required=True, help='primary keyword')
    ap.add_argument('--supporting', nargs='*', default=[])
    ap.add_argument('--max-keyword', type=int, default=5)
    ap.add_argument('--chunks', type=int, default=0, help='max words per humanizer part')
    ap.add_argument('--outdir', default='.')
    a = ap.parse_args()

    header, paras = load(a.docx)
    if not paras:
        sys.exit('No Heading 1 title found; is the title styled as Heading 1?')
    s = sections(paras)
    kw = a.keyword
    results = []

    def res(status, msg):
        results.append((status, msg))

    def ok(cond, msg, fail='FIX'):
        res('OK ' if cond else fail, msg)

    title = s['title']['text']
    body_paras = [p for sec in s['body'] for p in [sec['heading']] + sec['paras']]
    content = [s['title']] + s['intro'] + body_paras + ([s['conclusion_heading']] if 'conclusion_heading' in s else []) \
        + s['conclusion'] + ([s['faq_heading']] if 'faq_heading' in s else []) + s['faq']
    counted = [p for p in content if not READ_RE.match(p['text'])]
    all_text = '\n'.join(p['text'] for p in counted)
    wc = sum(words(p['text']) for p in counted)

    # 1. Length
    ok(wc <= 1500, f'Length {wc} words, body + FAQs (max 1,500)')
    if wc < 1000:
        res('WARN', f'Under the 1,000-1,500 target range ({wc} words)')

    # 2. Title and meta
    ok(len(title) < 60, f'Title {len(title)} characters (under 60): "{title}"')
    meta = re.sub(r'\s*\(\d+\s*characters?\)\s*$', '', header.get('meta description', ''))
    if meta:
        ok(140 <= len(meta) <= 160, f'Meta description {len(meta)} characters (140-160)')
    else:
        res('FIX', 'No "Meta description:" line above the title')

    # 3. Primary keyword placement
    slug = header.get('url slug', '')
    ok(count(title, kw) > 0, 'Primary keyword in title')
    if slug:
        ok(slugify(kw) in slug.lower() or all(w in slug.lower() for w in slugify(kw).split('-') if len(w) > 2),
           f'Primary keyword in URL slug ({slug})', 'WARN')
        ok(slug == slug.lower() and not re.search(r'\d{4}', slug), 'Slug lowercase, no dates', 'WARN')
    else:
        res('FIX', 'No "URL slug:" line above the title')
    first100 = ' '.join(' '.join(p['text'] for p in [s['title']] + s['intro'] + body_paras).split()[:100 + words(title)][words(title):])
    ok(count(first100, kw) > 0, 'Primary keyword in first 100 words')
    n_kw = count(all_text, kw)
    ok(n_kw <= a.max_keyword, f'Primary keyword "{kw}" used {n_kw} times (max {a.max_keyword}, no stuffing)')
    for sk in a.supporting:
        c = count(all_text, sk)
        ok(c > 0, f'Supporting keyword "{sk}" used {c} times', 'WARN')
    if a.supporting:
        faq_qs = ' '.join(p['text'] for p in s['faq'] if p['level'] == 3)
        ok(any(count(faq_qs, sk) for sk in a.supporting), 'A supporting keyword appears in at least one FAQ question', 'WARN')

    # 4. Structure
    iw = sum(words(p['text']) for p in s['intro'] if not READ_RE.match(p['text']))
    ok(80 <= iw <= 120, f'Introduction {iw} words (80-120)', 'WARN')
    ok(3 <= len(s['body']) <= 5, f'{len(s["body"])} body H2 sections (3-5)')
    levels = [p['level'] for p in paras if p['level']]
    skips = [f'H{x}->H{y}' for x, y in zip(levels, levels[1:]) if y > x + 1]
    ok(not skips, 'No skipped heading levels' + (f' ({", ".join(skips)})' if skips else ''))
    ok(sum(1 for l in levels if l == 1) == 1, 'Exactly one H1')
    cw = sum(words(p['text']) for p in s['conclusion'] if not READ_RE.match(p['text']))
    if 'conclusion_heading' in s:
        ok(60 <= cw <= 100, f'Conclusion {cw} words (60-100)', 'WARN')
        last = s['conclusion'][-1]['text'] if s['conclusion'] else ''
        ok(bool(CTA_RE.search(last)), 'Conclusion ends with a call to action', 'WARN')
    else:
        res('FIX', 'No conclusion section (H2 such as "Final thoughts")')
    ok(not s['refs'], 'No References section at the bottom')

    # 5. FAQs
    qs, answers, cur = [], [], None
    for p in s['faq']:
        if p['level'] == 3:
            qs.append(p['text']); answers.append([])
        elif answers:
            answers[-1].append(p)
    ok(len(qs) >= 2, f'{len(qs)} FAQs (at least 2)')
    for q, ans in zip(qs, answers):
        aw = sum(words(p['text']) for p in ans)
        lk = [l for p in ans for l in p['links']]
        ends_faq = bool(lk) and 'faq' in (lk[-1][0] + lk[-1][1]).lower()
        ok(40 <= aw <= 60, f'FAQ answer {aw} words (40-60): "{q[:50]}"', 'WARN')
        ok(ends_faq, f'FAQ answer ends with a link to the FAQ page: "{q[:50]}"')

    # 6. Links
    flat = [(p, l) for p in counted for l in p['links']]
    ext = [l for p, l in flat if l[1] and not any(d in l[1] for d in OWN_DOMAINS)]
    sol = [l for p, l in flat if 'appnable.com' in l[1] and '/blog' not in l[1] and 'faq' not in l[1].lower()]
    ok(len(ext) > 0, f'{len(ext)} inline source links')
    ok(len(sol) >= 1, f'{len(sol)} link(s) to an Appnable Solution page', 'FIX')
    for l in ext + sol:
        if re.match(r'^(click here|here|link|read more|this)$', l[0].strip(), re.I):
            res('WARN', f'Non-descriptive anchor text: "{l[0]}"')
    unlinked = [p['text'] for p in counted if p['level'] == 0 and re.search(r'\d+(\.\d+)?\s?(%|per cent|percent|million|billion|hours?)', p['text'])
                and not [l for l in p['links'] if l[1] and not any(d in l[1] for d in OWN_DOMAINS)]]
    for t in unlinked:
        res('WARN', f'Statistic without a source link in the same paragraph: "{t[:70]}..."')
    inline_ra = [p for p in paras if READ_RE.match(p['text']) and p not in s['readalso']]
    block_ra = [l for p in s['readalso'] for l in p['links']]
    if not inline_ra and not block_ra:
        res('INFO', 'No "Read also" links (allowed for the first one or two blogs)')
    else:
        ok(len(inline_ra) == 1, f'{len(inline_ra)} inline "Read also" link(s) mid-blog (1)', 'WARN')
        ok(2 <= len(block_ra) <= 3, f'{len(block_ra)} links in the "Read also" block (2-3)', 'WARN')
        for p in inline_ra + s['readalso']:
            for l in p['links']:
                if 'appnable.com' not in l[1] and 'kokoodi.com' not in l[1]:
                    res('FIX', f'"Read also" must link to an Appnable blog, not {l[1]}')

    # 7. Style
    body_text = [p for p in counted if p['level'] == 0]
    long_s = [x for p in body_text for x in re.split(r'(?<=[.!?])\s+', p['text']) if words(x) > 25]
    ok(len(long_s) <= 3, f'{len(long_s)} sentences over 25 words', 'WARN')
    for x in long_s[:5]:
        res('INFO', f'  long: "{x[:80]}..."')
    long_p = [p['text'] for p in body_text if len(re.findall(r'[.!?](\s|$)', p['text'])) > 4]
    ok(not long_p, f'{len(long_p)} paragraphs over 4 sentences', 'WARN')
    us = []
    for pat, fix in US_SPELLINGS.items():
        for m in re.finditer(pat, all_text, flags=re.I):
            us.append(f'{m.group(0)} -> {fix}')
    ok(not us, 'UK English (no US spellings found)' if not us else f'US spellings: {"; ".join(sorted(set(us)))}')
    low = all_text.lower()
    bn = [w for w in BANNED if re.search(r'(?<![a-z])' + re.escape(w) + r'(?![a-z])', low)]
    ok(not bn, 'No banned AI words (humanizing rules)' + (f': {", ".join(bn)}' if bn else ''))
    cl = [c for c in CLICHES if c in low and c not in bn]
    ok(not cl, 'No clichés / AI-sounding phrases' + (f': {", ".join(cl)}' if cl else ''), 'WARN')
    dashes = all_text.count('\u2014')
    ok(dashes <= 2, f'{dashes} em dashes (2 at most)')
    colon_leads = [p['text'] for p in body_text if re.match(r"^[A-Z][\w'’]*(\s[\w'’]+){0,3}:\s", p['text']) and not READ_RE.match(p['text'])]
    ok(len(colon_leads) <= 1, f'{len(colon_leads)} colon-led summary lines ("The result: ...")', 'WARN')
    triples = re.findall(r"\b(\w+(?: \w+){0,2}), (\w+(?: \w+){0,2}),? and (\w+(?: \w+){0,2})\b", ' '.join(p['text'] for p in body_text))
    ok(len(triples) <= 2, f'{len(triples)} possible rule-of-three lists in prose (keep to 2 or fewer)', 'WARN')
    for t in triples[:4]:
        res('INFO', f'  triple: "{t[0]}, {t[1]} and {t[2]}"')
    lens = [words(x) for p in body_text for x in re.split(r'(?<=[.!?])\s+', p['text']) if words(x) > 2]
    if len(lens) > 5:
        mean = sum(lens) / len(lens)
        sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
        ok(sd / mean >= 0.4, f'Sentence-length variety {sd / mean:.2f} (aim 0.40+; mix short and long sentences)', 'WARN')
    prose = [p['text'] for p in s['intro'][1:] + [q for sec in s['body'] for q in sec['paras']] + s['conclusion']
             if p['level'] == 0 and not READ_RE.match(p['text']) and words(p['text']) > 12]

    def opener(t):
        t = t.lower()
        return next((tr for tr in sorted(TRANSITIONS, key=len, reverse=True) if re.match(re.escape(tr) + r'\b', t)), None)
    ops = [opener(t) for t in prose]
    fil = [o for o in ops if o in FILLER]
    ok(not fil, 'No filler transitions (Furthermore, Moreover, Additionally)' + (f': {len(fil)} found' if fil else ''), 'WARN')
    reps = [o for o, n in zip(ops, ops[1:]) if o and o == n]
    ok(not reps, 'No transition repeated on consecutive paragraphs' + (f' ({", ".join(reps)})' if reps else ''), 'WARN')
    acr = []
    for m in re.finditer(r'\b[A-Z]{2,6}s?\b', all_text):
        tok = m.group(0).rstrip('s')
        if tok in ACRONYM_OK or tok in acr:
            continue
        if f'({tok})' not in all_text and f'({tok}s)' not in all_text:
            acr.append(tok)
    ok(not acr, 'Acronyms explained on first use' + (f' (check: {", ".join(acr)})' if acr else ''), 'WARN')
    # 8. Appnable specifics: selling section, cover image, stats phrasing, ERP claim
    sell = [i for i, sec in enumerate(s['body']) if OWN_NAMES.search(' '.join(p['text'] for p in [sec['heading']] + sec['paras']))]
    ok(bool(sell), 'Mid-blog selling section (a body section about Appnable, KoKoodi or StGatherly)')
    if sell and len(s['body']) >= 3:
        mid = [i for i in sell if 0 < i < len(s['body']) - 1]
        ok(bool(mid), f'Selling section sits mid-blog (found in body section {sell[0] + 1} of {len(s["body"])})', 'WARN')
    cover = header.get('cover image', '')
    ok(bool(cover) and any(d in cover.lower() for d in IMAGE_DOMAINS),
       'Cover image source credited from an approved library' if cover else 'No "Cover image:" line with an approved source above the title')
    ok(bool(header.get('cover image alt text')), 'Cover image alt text given', 'WARN')
    if ext:
        ok(any(re.search(r'stats by', l[0], re.I) for l in ext), '"According to stats by [Source]" phrasing used for a statistic', 'WARN')
    dyn = [p['text'] for p in counted if 'dynamics 365' in p['text'].lower() and OWN_NAMES.search(p['text'])]
    ok(not dyn, 'No claim that Appnable implements Dynamics 365 (Appnable implements Odoo)', 'WARN')
    ok(N_IMAGES >= 1, f'{N_IMAGES} image(s) or diagram(s) in the blog (a story-telling visual, e.g. the workflow illustration)', 'WARN')
    diy = re.search(r"\b(diy|do-it-yourself|yourself|in-house|on your own|stalls?|go(es)? wrong|fails?|pitfalls?|why .*appnable|where .* (fail|stall))", ' '.join(sec['heading']['text'] for sec in s['body']), re.I)
    ok(bool(diy), 'A body section on why Appnable rather than DIY (e.g. "Where DIY ... stalls")', 'WARN')
    res('INFO', 'Still for people: images (<200 KB, alt text), SME technical review, marketing review, Grammarly UK, read aloud, FAQ page match')

    print(f'Blog: {title}')
    for st, msg in results:
        print(f'[{st}] {msg}')
    fixes = sum(1 for st, _ in results if st == 'FIX')
    print(f'\n{fixes} FIX item(s), {sum(1 for st, _ in results if st == "WARN")} WARN item(s)')

    if a.chunks:
        os.makedirs(a.outdir, exist_ok=True)
        n = max(1, math.ceil(wc / a.chunks))
        goal = wc / n
        parts, cur, cur_w = [], [], 0
        for p in counted:
            w = words(p['text'])
            if cur and ((p['level'] and cur_w >= goal * 0.85 and len(parts) < n - 1) or cur_w + w > a.chunks):
                parts.append(cur); cur, cur_w = [], 0
            cur.append(p); cur_w += w
        if cur:
            parts.append(cur)
        base = os.path.splitext(os.path.basename(a.docx))[0]
        for i, part in enumerate(parts, 1):
            text = '\n\n'.join(p['text'] for p in part)
            fn = os.path.join(a.outdir, f'{base}_part{i}.txt')
            open(fn, 'w').write(text)
            print(f'Part {i}: {words(text)} words, primary keyword x{count(text, kw)} -> {fn}')


if __name__ == '__main__':
    main()
