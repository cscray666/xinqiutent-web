const fs = require("fs");
for (const f of process.argv.slice(2)) {
  const obj = JSON.parse(fs.readFileSync(f, "utf8"));
  console.log("=== " + f.split("\\").pop());
  console.log("recordCount:", obj.data.recordCount, "| url:", obj.data.downloadUrl);
  for (const p of obj.data.data) {
    console.log(JSON.stringify({id: p.id, name: (p.prodName||"").slice(0,60), vis: p.sumProdVisitorCnt, mcFbUv: p.mcFbUv, sumProdFbNum: p.sumProdFbNum, atmFbUv: p.atmFbUv, crtOrd: p.crtOrd, rtsOnlineAmt: p.rtsOnlineAmt, coc: p.sumProdVisitorCntCoc}));
  }
}
