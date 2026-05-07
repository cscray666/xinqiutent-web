(async () => {
  const viewsChart = document.querySelector('.js-graph.traffic-graph[data-graph-name="visitors"]');
  const clonesChart = document.querySelector('.js-graph.traffic-graph[data-graph-name="clones"]');
  
  // Data is often stored in data attributes or can be extracted from the SVG
  // But usually, GitHub traffic charts are SVG rendered.
  // We can try to find the last data point in the SVG.
  
  function getLatestData(selector) {
    const svg = document.querySelector(selector + ' svg');
    if (!svg) return null;
    // GitHub graphs use tooltips. We might need to look at the circles or paths.
    // Or check if there's a data table.
    return "Check snapshot or tables";
  }

  // Actually, there's a "View as data table" button. Let's try to click it or find the table.
  const viewAsTableButtons = document.querySelectorAll('button[aria-label^="View as data table"]');
  if (viewAsTableButtons.length > 0) {
    // This is for accessibility, it might reveal a hidden table.
  }

  return {
    viewsLastPoint: document.querySelector('.js-graph.traffic-graph[data-graph-name="visitors"] .js-graph-data') ? "Found data" : "No data element",
    referringSites: Array.from(document.querySelectorAll('table[aria-label="Referring sites"] tbody tr')).map(tr => tr.innerText),
    popularContent: Array.from(document.querySelectorAll('table[aria-label="Popular content"] tbody tr')).map(tr => tr.innerText)
  };
})()