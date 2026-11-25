#!/usr/bin/env python3 -I
"""Rebuild js/search-index.json from papers.html + the site's pages.

Run from anywhere:  python3 -I _tools/build-search-index.py
Needs the PDF extractor compiled once (macOS):
    swiftc -O _tools/pdf2txt.swift -o _tools/pdf2txt
Word/RTF/HTML files are read with macOS `textutil`. Slides (.ppt) are skipped.
Paper titles, summaries and years come from papers.html (rows with data-y).
"""
import html, json, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF2TXT = os.path.join(ROOT, '_tools', 'pdf2txt')
PAGES = ['index.html', 'quantum-1f-noise.html', 'gan-devices.html', 'atmospheric-physics.html',
         'sensors.html', 'oscillators.html', 'nanotechnology.html', 'astrophysics-cosmology.html',
         'QuantumBib.html', 'cv.htm', 'research.htm', 'synopsis.htm', 'handelp.html']


def clean(t, cap):
    t = ''.join(c if c.isprintable() else ' ' for c in t)
    # drop binary junk: overly long tokens or tokens that are mostly non-alphanumeric
    toks = [w for w in t.split() if len(w) < 40 and sum(ch.isalnum() for ch in w) >= max(1, len(w) * 0.6)]
    return ' '.join(toks)[:cap]


def extract(path):
    ext = path.lower().rsplit('.', 1)[-1]
    try:
        if ext == 'pdf':
            return subprocess.run([PDF2TXT, path], capture_output=True, text=True, timeout=120).stdout
        if ext in ('doc', 'docx', 'rtf', 'htm', 'html'):
            return subprocess.run(['textutil', '-convert', 'txt', '-stdout', path],
                                  capture_output=True, text=True, timeout=120).stdout
    except Exception as e:
        print('  ! could not read', path, e, file=sys.stderr)
    return ''


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def main():
    os.chdir(ROOT)
    if not os.path.exists(PDF2TXT):
        sys.exit('Compile the extractor first: swiftc -O _tools/pdf2txt.swift -o _tools/pdf2txt')
    src = open('papers.html', encoding='utf-8').read()
    rows = re.findall(r'<tr class="hd" id="p\w+" data-n="\w+" data-y="(\d*)"><td class="n">#(\w+)</td>'
                      r'<td>(.*?)</td><td class="lk">(.*?)</td></tr>\s*'
                      r'<tr class="sm[^"]*"><td></td><td colspan="2">(.*?)</td></tr>', src, re.S)
    docs = []
    for y, n, title, links_html, summ in rows:
        links = re.findall(r'href="([^"]+)"', links_html)
        if not links:
            continue
        text = ''
        for l in links:
            text = extract(urllib.parse.unquote(html.unescape(l)))
            if text.strip():
                break
        title = re.sub(r'<span class="yr">.*?</span>', '', title)
        docs.append(dict(k='paper', n=n.rstrip('_'), t=strip_tags(title).rstrip(',;:').strip(), u=links[0],
                         s=strip_tags(re.sub(r'Show more', '', summ)), x=clean(text, 40000),
                         y=int(y) if y else None))
        print(f'#{n:6} {len(docs[-1]["x"]):6} chars  {links[0]}')
    for p in PAGES:
        s = open(p, encoding='utf-8', errors='replace').read()
        m = re.search(r'<title>(.*?)</title>', s, re.S)
        body = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', s)
        docs.append(dict(k='page', t=html.unescape(m.group(1)).strip() if m else p, u=p, s='',
                         x=clean(html.unescape(re.sub(r'<[^>]+>', ' ', body)), 60000)))
    out = json.dumps(docs, ensure_ascii=False, separators=(',', ':'))
    open('js/search-index.json', 'w', encoding='utf-8').write(out)
    print(f'{len(docs)} docs, {len(out) // 1024} KB -> js/search-index.json')


if __name__ == '__main__':
    main()
