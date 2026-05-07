(() => {
  const item = document.querySelector('#zg-ordered-list li, .zg-grid-general-faceout, [id^="p13n-asin-index-"]');
  if (!item) return { error: "No items found" };

  const nameEl = item.querySelector('div[class*="_p13n-zg-list-grid-desktop_style_zg-force-grid-column"] ._p13n-zg-list-grid-desktop_style_zg-cg-executable-text__2S8m1, .p13n-sc-truncated, ._cDEo1_truncate_3_689S, .a-link-normal div:nth-child(2)');
  const linkEl = item.querySelector('a.a-link-normal');
  const ratingEl = item.querySelector('.a-icon-row .a-icon-alt, .a-star-small .a-icon-alt');
  const reviewCountEl = item.querySelector('.a-size-small.a-color-secondary, .a-size-small .a-link-normal');
  const priceEl = item.querySelector('.p13n-sc-price, ._cDEo1_price_16-S6');

  // Alternative for the new grid layout
  const title = item.querySelector('.p13n-sc-truncate-desktop-type2, .p13n-sc-truncated')?.innerText || 
                item.querySelector('a.a-link-normal div')?.innerText ||
                item.querySelector('span div')?.innerText;
  
  const href = linkEl?.href;
  const rating = ratingEl?.innerText;
  const reviewCount = reviewCountEl?.innerText;
  const price = priceEl?.innerText;

  return {
    name: title?.trim(),
    url: href,
    rating,
    reviewCount,
    price,
    raw: item.innerText
  };
})()