const fs = require('fs');
const path = require('path');

const indexHtml = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const newsHtml = fs.readFileSync(path.join(__dirname, 'news.html'), 'utf8');

const indexBase64 = Buffer.from(indexHtml).toString('base64');
const newsBase64 = Buffer.from(newsHtml).toString('base64');

// Split base64 strings into chunks of 1000 characters
function chunkString(str, size) {
  const numChunks = Math.ceil(str.length / size);
  const chunks = new Array(numChunks);
  for (let i = 0, o = 0; i < numChunks; ++i, o += size) {
    chunks[i] = str.substr(o, size);
  }
  return chunks;
}

const indexChunks = chunkString(indexBase64, 1000);
const newsChunks = chunkString(newsBase64, 1000);

const indexChunksJs = indexChunks.map(c => `  "${c}"`).join(',\n');
const newsChunksJs = newsChunks.map(c => `  "${c}"`).join(',\n');

const scriptContent = `(async () => {
  try {
    const indexB64 = [
${indexChunksJs}
    ].join("");

    const newsB64 = [
${newsChunksJs}
    ].join("");

    function b64ToUint8Array(b64) {
      const binaryString = atob(b64);
      const len = binaryString.length;
      const bytes = new Uint8Array(len);
      for (let i = 0; i < len; i++) {
        bytes[i] = binaryString.charCodeAt(i);
      }
      return bytes;
    }

    const indexBytes = b64ToUint8Array(indexB64);
    const indexBlob = new Blob([indexBytes], { type: "text/html" });
    const indexFile = new File([indexBlob], "index.html", { type: "text/html" });

    const newsBytes = b64ToUint8Array(newsB64);
    const newsBlob = new Blob([newsBytes], { type: "text/html" });
    const newsFile = new File([newsBlob], "news.html", { type: "text/html" });

    const input = document.getElementById("upload-manifest-files-input");
    if (!input) {
      window.uploadResult = { success: false, error: "Input element not found" };
      return;
    }

    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(indexFile);
    dataTransfer.items.add(newsFile);
    input.files = dataTransfer.files;

    input.dispatchEvent(new Event("change", { bubbles: true }));
    console.log("Attached files and dispatched change event.");

    // Wait 10 seconds for files to process and upload
    await new Promise(resolve => setTimeout(resolve, 10000));

    const commitSummary = document.getElementById("commit-summary-input");
    if (commitSummary) {
      commitSummary.value = "Fix: Force upload of index.html and news.html to recover truncated build";
      commitSummary.dispatchEvent(new Event("input", { bubbles: true }));
      commitSummary.dispatchEvent(new Event("change", { bubbles: true }));
      console.log("Filled commit summary.");
    }

    const directRadio = document.querySelector('input[type="radio"][value="direct"]');
    if (directRadio && !directRadio.checked) {
      directRadio.click();
      console.log("Selected direct commit.");
    }

    const submitButton = Array.from(document.querySelectorAll('button[type="submit"]')).find(
      b => b.textContent.includes("提交更改") || b.textContent.includes("Commit changes")
    );

    if (submitButton) {
      console.log("Submitting form...");
      submitButton.click();
      window.uploadResult = { success: true };
    } else {
      window.uploadResult = { success: false, error: "Submit button not found" };
    }
  } catch (err) {
    window.uploadResult = { success: false, error: err.name + ": " + err.message };
  }
})();`;

fs.writeFileSync(path.join(__dirname, 'final_upload.js'), scriptContent, 'utf8');
console.log('Successfully generated final_upload.js with chunked strings');
