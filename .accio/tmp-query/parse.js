const fs = require("fs");
const files = process.argv.slice(2);
for (const f of files) {
  const obj = JSON.parse(fs.readFileSync(f, "utf8"));
  console.log("=== " + f.split("\\").pop() + " success=" + obj.success + " count=" + obj.data.length);
  for (const d of obj.data) {
    console.log(JSON.stringify({
      statDate: d.statDate, uvCnt: d.uvCnt, pvCnt: d.pvCnt, fbUv: d.fbUv, fbTmUv: d.fbTmUv,
      sucOrdAmt: d.sucOrdAmt, sucOrdCnt: d.sucOrdCnt,
      hasUv: Object.prototype.hasOwnProperty.call(d,"uvCnt"), hasPv: Object.prototype.hasOwnProperty.call(d,"pvCnt"),
      hasFbUv: Object.prototype.hasOwnProperty.call(d,"fbUv"), hasFbTmUv: Object.prototype.hasOwnProperty.call(d,"fbTmUv"),
      hasAmt: Object.prototype.hasOwnProperty.call(d,"sucOrdAmt"), hasCnt: Object.prototype.hasOwnProperty.call(d,"sucOrdCnt")
    }));
  }
}
