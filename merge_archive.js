// Merge EN skeleton + ZH translations into final bilingual document
const fs = require('fs');
const articles = require('./news_articles_extracted.json');
const zh1 = require('./_zh_part1.json');
const zh2 = require('./_zh_part2.json');
const zh3 = require('./_zh_part3.json');
const ZH = Object.assign({}, zh1, zh2, zh3);

const seen = new Set();
const uniq = articles.filter(a => { if (seen.has(a.id)) return false; seen.add(a.id); return true; });
uniq.sort((a, b) => parseInt(a.id) - parseInt(b.id));

function clean(text) {
  return text
    .replace(/<img[^>]*>/g, '')
    .replace(/<h2[^>]*>/g, '\n## ')
    .replace(/<\/h2>/g, '\n')
    .replace(/<h3[^>]*>/g, '\n### ')
    .replace(/<\/h3>/g, '\n')
    .replace(/<li[^>]*>/g, '\n- ')
    .replace(/<\/li>/g, '')
    .replace(/<strong>/g, '**').replace(/<\/strong>/g, '**')
    .replace(/<[^>]+>/g, '')
    .replace(/\\"/g, '"')
    .replace(/\\'/g, "'")
    .replace(/[ \t]+/g, ' ')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

let doc = `# XINQIU TENT 独立站全部行业文章 · 中英双语完整版
# XINQIU TENT Full Article Archive (Complete Bilingual Version)

> 本文件收录 www.xinqiutent.com 已发布的全部 ${uniq.length} 篇行业文章（英文原文 + 中文翻译）。
> This file contains all ${uniq.length} published industry articles (English original + Chinese translation).
> 生成日期 Generated: 2026-08-11

---

`;

for (const a of uniq) {
  const zh = ZH[a.id] || { t: '(translation pending)', b: '(translation pending)' };
  doc += `## 第 ${a.id} 篇 · Published ${a.date}
## Article #${a.id} · Published ${a.date}

### 英文标题 (English Title)
**${a.title}**

### 中文标题 (Chinese Title)
**${zh.t}**

### 英文原文 (English Original)
${clean(a.body)}

### 中文翻译 (Chinese Translation)
${zh.b}

---

`;
}

fs.writeFileSync('独立站全部文章_中英双语完整版.md', doc, 'utf8');
console.log('FINAL document generated:', doc.length, 'chars for', uniq.length, 'articles');
