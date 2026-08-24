const fs = require("fs"), path = require("path");
const dir = process.argv[2];
const files = fs.readdirSync(dir).filter(f => f.endsWith(".txt"));
const agg = new Map(); // id -> {name, vis, mcFbUv, fbNum, atmFbUv, crtOrd, rtsAmt, days:Set}
for (const f of files) {
  let obj; try { obj = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")); } catch(e) { continue; }
  if (!obj || !obj.data || !obj.data.data) continue;
  const url = obj.data.downloadUrl || "";
  const m = url.match(/statDate=([\d-]+)/);
  const isDay = url.includes("statisticsType=day");
  if (!isDay || !m) continue;
  const d = m[1];
  if (!(d >= "2026-08-17" && d <= "2026-08-22")) continue;
  for (const p of obj.data.data) {
    let e = agg.get(p.id);
    if (!e) { e = {id: p.id, name: p.prodName || p.subject, vis:0, mcFbUv:0, fbNum:0, atmFbUv:0, crtOrd:0, rtsAmt:0, days:new Set()}; agg.set(p.id, e); }
    e.vis += p.sumProdVisitorCnt||0; e.mcFbUv += p.mcFbUv||0; e.fbNum += p.sumProdFbNum||0;
    e.atmFbUv += p.atmFbUv||0; e.crtOrd += p.crtOrd||0; e.rtsAmt += p.rtsOnlineAmt||0; e.days.add(d);
  }
}
const rows = [...agg.values()].sort((a,b)=>b.vis-a.vis);
console.log("distinct products:", rows.length);
for (const r of rows.slice(0, 12)) {
  console.log(JSON.stringify({id: r.id, name: r.name.slice(0,55), vis: r.vis, mcFbUv: r.mcFbUv, fbNum: r.fbNum, atmFbUv: r.atmFbUv, crtOrd: r.crtOrd, rtsAmt: r.rtsAmt, days: [...r.days].sort().join(",")}));
}
