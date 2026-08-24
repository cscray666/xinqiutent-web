const fs = require("fs");
const obj = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
console.log("recordCount:", obj.data.recordCount);
console.log("downloadUrl:", obj.data.downloadUrl);
for (const p of obj.data.data) {
  console.log(JSON.stringify({
    id: p.id, prodName: p.prodName, subject: p.subject, priceRange: p.priceRange,
    sumProdVisitorCnt: p.sumProdVisitorCnt, visitors: p.visitors,
    sumProdFbNum: p.sumProdFbNum, mcFbUv: p.mcFbUv, inquiries: p.inquiries,
    atmFbUv: p.atmFbUv, crtOrd: p.crtOrd, rtsOnlineAmt: p.rtsOnlineAmt,
    sumProdShowNum: p.sumProdShowNum, totalImpsCnt: p.totalImpsCnt, totalClkCnt: p.totalClkCnt,
    sumProdVisitorCntCoc: p.sumProdVisitorCntCoc, sumProdFbRate: p.sumProdFbRate
  }));
  // 输出所有 key，检查是否有支付订单/金额字段
  const keys = Object.keys(p);
  const payKeys = keys.filter(k => /suc|ord|amt|pay/i.test(k));
  console.log("  pay-related keys:", JSON.stringify(payKeys));
  console.log("  all keys count:", keys.length);
}
