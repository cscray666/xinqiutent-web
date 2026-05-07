(async () => {
  const text = document.body.innerText;
  const match = text.match(/G-[A-Z0-9]{5,}/g);
  return { id: match ? match[0] : null, all: match };
})()