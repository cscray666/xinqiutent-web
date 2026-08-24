(() => {
  const clean = (s) => s ? s.replace(/\s+/g, ' ').trim() : null;
  const text = (sel) => { const el = document.querySelector(sel); return el ? clean(el.textContent) : null; };
  const bodyText = document.body.innerText;

  const title = text('#productTitle');

  // price: buybox main price
  let price = null;
  const priceEl = document.querySelector('#corePriceDisplay_desktop_feature_div .a-offscreen') ||
                  document.querySelector('.apexPriceToPay .a-offscreen') ||
                  document.querySelector('#priceblock_ourprice');
  if (priceEl) price = clean(priceEl.textContent);

  const prime = !!(document.querySelector('#prime-badge, .a-icon-prime, .a-icon-prime-all, [alt="Prime"], [aria-label*="Prime"]'));

  // merchant info line in buybox
  let merchant = null;
  const buybox = document.querySelector('#buybox, #desktop_buybox');
  if (buybox) {
    const bbText = buybox.textContent.replace(/\s+/g, ' ');
    const m = bbText.match(/(?:来自|Verkauft von|Sold by|由).{0,3}([\u4e00-\u9fa5A-Za-z0-9®©.\s]{1,40}?)(?:返回|Verk\u00e4ufer|通过|发货|Versand|,\s*Versand|$)/);
    if (m) merchant = clean(m[1]);
  }
  const versandAmazon = bodyText.includes('Versand durch Amazon') || bodyText.includes('来自 亚马逊') || bodyText.includes('由亚马逊配送') || bodyText.includes('亚马逊发货') || bodyText.includes('Amazon 配送') || bodyText.includes('Dispatched from Amazon');
  const verkauftAmazon = bodyText.includes('Verkauf durch Amazon') || bodyText.includes('由亚马逊销售') || bodyText.includes('亚马逊销售');

  let delivery = null;
  const deliv = document.querySelector('#deliveryBlockMessage, #mir-layout-DELIVERY_BLOCK, #delivery-block-primary, #ddmDeliveryMessage');
  if (deliv) delivery = clean(deliv.textContent);

  const rating = text('#acrPopover .a-icon-alt');
  const reviewCountRaw = text('#acrCustomerReviewText') || text('#acrCustomerReviewLink');

  // monthly purchases: German or Chinese UI patterns
  const monthlyMatch = bodyText.match(/([\d.,\s]+)\s*\+?\s*mal im letzten Monat gekauft/) ||
                       bodyText.match(/([\d.,\s]+)\s*\+?\s*(?:过去一个月内|过去30天内)\s*购买/) ||
                       bodyText.match(/([\d.,\s]+)\s*\+?\s*(?:purchased|bought)\s*in the past month/i);
  const monthly = monthlyMatch ? monthlyMatch[1].replace(/[^\d.,]/g, '').trim() : null;

  // weight / dimensions
  let weight = null, dims = null;
  const detailNodes = document.querySelectorAll('#productDetails_techSpec_section_1 tr, #productDetails_detailBullets_sections1 tr, #detailBullets_feature_div li, #productOverview_feature_div tr, #prodDetails tr');
  detailNodes.forEach(r => {
    const t = clean(r.textContent);
    if (!t) return;
    if (/(gewicht|weight|物品重量|商品重量)/i.test(t) && !weight) weight = t;
    if (/(abmessungen|ma\u00dfe|dimensions|产品尺寸|商品尺寸)/i.test(t) && !dims) dims = t;
  });
  // fallback: the fact-list above about this item (物品重量/产品尺寸 shown as list)
  if (!weight || !dims) {
    const ov = document.querySelector('#productOverview_feature_div, #detailBullets_feature_div');
    if (ov) {
      const pairs = Array.from(ov.querySelectorAll('li, tr, .a-row')).map(e => clean(e.textContent)).filter(Boolean);
      pairs.forEach(t => {
        if (!weight && /(gewicht|weight|物品重量)/i.test(t)) weight = t;
        if (!dims && /(abmessungen|ma\u00dfe|dimensions|产品尺寸)/i.test(t)) dims = t;
      });
    }
  }

  const avail = text('#availability');
  const inStock = !!(document.querySelector('#add-to-cart-button') || document.querySelector('#buy-now-button'));
  const unavailableText = bodyText.includes('Derzeit nicht verfügbar') || bodyText.includes('目前无法购买') || bodyText.includes('currently unavailable') || bodyText.includes('无报价');

  return { url: location.href, title, price, prime, merchant, versandAmazon, verkauftAmazon, delivery, rating, reviewCountRaw, monthly, weight, dims, avail, inStock, unavailableText };
})()
