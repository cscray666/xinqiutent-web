(() => {
  const items = Array.from(document.querySelectorAll('.product-item, .component-product-list-item, .list-item'));
  const products = [];
  
  // Alternative selector for Alibaba shop pages
  const productCards = document.querySelectorAll('.icbu-shop-product-list .item-content');
  const cards = productCards.length > 0 ? Array.from(productCards) : Array.from(document.querySelectorAll('.product-card, [class*="product-item"]'));

  cards.forEach(card => {
    const titleEl = card.querySelector('.title, [class*="title"]');
    const linkEl = card.querySelector('a');
    const imgEl = card.querySelector('img');
    const priceEl = card.querySelector('.price, [class*="price"]');
    const orderEl = card.querySelector('.order, [class*="order"], .sold');

    if (titleEl && linkEl) {
      const title = titleEl.textContent.trim();
      const url = linkEl.href;
      const img = imgEl ? imgEl.src : '';
      const orders = orderEl ? orderEl.textContent.trim() : '';
      
      products.push({ title, url, img, orders });
    }
  });

  return products;
})()