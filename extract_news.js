// Extract all news articles from news.html for the bilingual archive
const fs = require('fs');
const html = fs.readFileSync('news.html', 'utf8');

// Find the newsData object
const start = html.indexOf('const newsData = {');
const end = html.indexOf('};', start);
const objStr = html.slice(start + 'const newsData = {'.length, end);

// Simple extraction of each article block
const blocks = [];
const re = /'(\d+)':\s*\{([\s\S]*?)\n\s*\}/g;
let m;
while ((m = re.exec(objStr)) !== null) {
  const id = m[1];
  const block = m[2];
  const titleMatch = block.match(/title:\s*"([^"]+)"/);
  const dateMatch = block.match(/date:\s*"([^"]+)"/);
  const bodyMatch = block.match(/body:\s*`([\s\S]*?)`/);
  blocks.push({
    id,
    title: titleMatch ? titleMatch[1] : '',
    date: dateMatch ? dateMatch[1] : '',
    body: bodyMatch ? bodyMatch[1].trim() : ''
  });
}

blocks.sort((a, b) => parseInt(a.id) - parseInt(b.id));

// Write a JSON for further processing
fs.writeFileSync('news_articles_extracted.json', JSON.stringify(blocks, null, 2));
console.log('Extracted articles:', blocks.length);
blocks.forEach(b => console.log(`${b.id}: ${b.date} | ${b.title.slice(0, 60)}`));
