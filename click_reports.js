(async () => {
  const reportsLink = Array.from(document.querySelectorAll('a')).find(a => a.innerText.includes('报告') || a.innerText.includes('Reports'));
  if (reportsLink) {
    reportsLink.click();
    return "Clicked Reports link";
  }
  return "Reports link not found";
})()