// Generate the full bilingual archive document (EN + ZH for every article)
const fs = require('fs');
const articles = require('./news_articles_extracted.json');

// Deduplicate by id (keep first occurrence)
const seen = new Set();
const uniq = articles.filter(a => { if (seen.has(a.id)) return false; seen.add(a.id); return true; });

// Clean HTML tags and trim
function clean(text) {
  return text
    .replace(/<[^>]+>/g, ' ')   // strip tags
    .replace(/\s+/g, ' ')
    .trim();
}

let doc = `# XINQIU TENT 独立站全部行业文章 · 中英双语完整版
# XINQIU TENT Website Full Article Archive (Complete Bilingual Version)

> 本文件收录独立站 www.xinqiutent.com 已发布的所有行业文章（含英文原文与中文翻译）。
> 生成时间：2026-08-11 | 共 ${uniq.length} 篇
>
> This file contains every published industry article from www.xinqiutent.com with both English original text and Chinese translation.

---

`;

for (const a of uniq) {
  const bodyEn = clean(a.body);
  // Placeholder: Chinese translation inserted below per article
  doc += `## #${a.id} · ${a.date}
## ${a.title}

### EN (English Original)
${bodyEn}

### ZH (中文翻译)
${ZH_MAP[a.id] || '(translation pending)'}

---
`;
}

fs.writeFileSync('_archive_zh_placeholder.md', doc);
console.log('Generated placeholder doc with', uniq.length, 'articles');
console.log('Total chars:', doc.length);
