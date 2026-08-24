# -*- coding: utf-8 -*-
import re
from pypdf import PdfReader

r = PdfReader('Xinqiu-Company-Profile-Wanderfalke-2026-08.pdf')
print('PAGES:', len(r.pages))
txt = ''.join(p.extract_text() or '' for p in r.pages)
cjk = re.findall(r'[\u4e00-\u9fff]', txt)
print('CJK_COUNT:', len(cjk), ''.join(sorted(set(cjk))))
checks = ['36', '24', '200,000', '20,000', '16 total', '300 units', '3,300',
          '15,000', '30%', '20%', '15%', '35%', '45 days', '3.5 hours',
          '30 minutes', 'BSCI', 'SGS', 'Anhui', 'Page 1']
for n in checks:
    print(('OK  ' if n in txt else 'MISS'), n)
print('LEAK internal:', 'internal' in txt.lower(),
      '| Carrefour:', 'Carrefour' in txt, '| ISO:', 'ISO' in txt)
print('TAIL:', repr(txt[-300:]))
