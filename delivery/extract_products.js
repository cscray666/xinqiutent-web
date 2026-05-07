(async () => {
  const items = Array.from(document.querySelectorAll('.search-item, .list-no-v2-main, .grid-item, [data-content="productItem"]'));
  const results = items.map(item => {
    const titleEl = item.querySelector('.search-card-e-title, h2, .title');
    const priceEl = item.querySelector('.search-card-e-price-main, .price');
    const ordersEl = item.querySelector('.search-card-e-order, .sale-info');
    const supplierEl = item.querySelector('.search-card-e-company, .company-name');
    const supplierYearsEl = item.querySelector('.search-card-e-supplier-years, .years');
    
    return {
      title: titleEl ? titleEl.innerText.trim() : '',
      price: priceEl ? priceEl.innerText.trim() : '',
      orders: ordersEl ? ordersEl.innerText.trim() : '',
      supplier: supplierEl ? supplierEl.innerText.trim() : '',
      years: supplierYearsEl ? supplierYearsEl.innerText.trim() : '',
      url: titleEl && titleEl.closest('a') ? titleEl.closest('a').href : ''
    };
  }).filter(item => item.title);
  
  return results;
})()