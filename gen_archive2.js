// Generate the complete bilingual archive (EN auto-extracted + ZH placeholder structure)
const fs = require('fs');
const articles = require('./news_articles_extracted.json');

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

const EN = {};
for (const a of uniq) {
  EN[a.id] = clean(a.body);
}

fs.writeFileSync('_articles_en.json', JSON.stringify(EN, null, 2));

// Generate the skeleton document
let doc = `# XINQIU TENT 独立站全部行业文章 · 中英双语完整版
# XINQIU TENT Full Article Archive (Complete Bilingual Version)

> 本文件收录 www.xinqiutent.com 已发布的全部 ${uniq.length} 篇行业文章（英文原文 + 中文翻译）。
> This file contains all ${uniq.length} published industry articles (English original + Chinese translation).
> 生成日期 Generated: 2026-08-11

---

`;

for (const a of uniq) {
  doc += `## 第 ${a.id} 篇 · Published ${a.date}
## Article #${a.id} · Published ${a.date}

### 英文标题 (English Title)
**${a.title}**

### 中文标题 (Chinese Title)
<!-- ZH_TITLE_${a.id} -->

### 英文原文 (English Original)
${EN[a.id]}

### 中文翻译 (Chinese Translation)
<!-- ZH_BODY_${a.id} -->

---

`;
}

fs.writeFileSync('独立站全部文章_中英双语完整版.md', doc);
console.log('Skeleton generated:', doc.length, 'chars for', uniq.length, 'articles');
