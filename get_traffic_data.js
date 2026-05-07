
(async () => {
  const scripts = Array.from(document.querySelectorAll('script[type="application/json"]'));
  const trafficData = scripts.find(s => s.textContent.includes('traffic'));
  if (trafficData) {
    return JSON.parse(trafficData.textContent);
  }
  
  // Fallback: Try to find data in the graph components if they have tooltips or similar
  // Or just look at the last data point in the SVG if possible
  return { error: "JSON data not found" };
})()
