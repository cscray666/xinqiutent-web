const fs = require("fs"), path = require("path");
const dir = process.argv[2];
const ids = ["RmV7kzT7MBKYpGWekpGY5413","pAQS6QfOMJ8SC8Qg8OoA5995","P0lLkOlIMFIEISSEurFX9406","zyZ6b7w9kULaYvFMchAR8619","Oj2HgO31m6yGetGjt1Jd5755","b82D5ljZrbxCJNeM6JeH7431"];
const files = fs.readdirSync(dir).filter(f => f.endsWith(".txt") && ids.some(id => f.includes(id))).map(f => path.join(dir, f));
const agg = new Map();
for (const f of files) {
  let obj; try { obj = JSON.parse(fs.readFileSync(f, "utf8")); } catch(e) { console.log("PARSE FAIL", path.basename(f), e.message); continue; }
  const url = obj.data.downloadUrl || "";
  const m = url.match(/statDate=([\d-]+)/); if (!m) continue;
  const d = m[1];
  for (const p of obj.data.data) {
    let e = agg.get(p.id);
    if (!e) { e = {id: p.id, name: p.prodName || p.subject, vis:0, mcFbUv:0, fbNum:0, atmFbUv:0, crtOrd:0, rtsAmt:0, days:0, dates:[]}; agg.set(p.id, e); }
    e.vis += p.sumProdVisitorCnt||0; e.mcFbUv += p.mcFbUv||0; e.fbNum += p.sumProdFbNum||0;
    e.atmFbUv += p.atmFbUv||0; e.crtOrd += p.crtOrd||0; e.rtsAmt += p.rtsOnlineAmt||0; e.days++; e.dates.push(d);
  }
}
const rows = [...agg.values()].sort((a,b)=>b.vis-a.vis);
console.log("parsed files:", files.length, "| distinct products:", rows.length);
for (const r of rows.slice(0, 8)) {
  console.log(JSON.stringify({id: r.id, name: r.name.slice(0,60), vis: r.vis, fbNum: r.fbNum, mcFbUv: r.mcFbUv, atmFbUv: r.atmFbUv, crtOrd: r.crtOrd, rtsAmt: r.rtsAmt, days: r.days}));
}
