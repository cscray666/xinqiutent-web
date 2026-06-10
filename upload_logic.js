(async () => {
  try {
    console.log("Fetching index.html...");
    const resIndex = await fetch("http://localhost:9999/index.html");
    const blobIndex = await resIndex.blob();
    const fileIndex = new File([blobIndex], "index.html", { type: "text/html" });

    console.log("Fetching news.html...");
    const resNews = await fetch("http://localhost:9999/news.html");
    const blobNews = await resNews.blob();
    const fileNews = new File([blobNews], "news.html", { type: "text/html" });

    const input = document.getElementById("upload-manifest-files-input");
    if (!input) {
      console.error("File input not found!");
      return "ERROR: File input not found";
    }

    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(fileIndex);
    dataTransfer.items.add(fileNews);
    input.files = dataTransfer.files;

    input.dispatchEvent(new Event("change", { bubbles: true }));
    console.log("Files set and change event dispatched.");

    // Wait for the files to process
    await new Promise(resolve => setTimeout(resolve, 8000));

    const commitSummary = document.getElementById("commit-summary-input");
    if (commitSummary) {
      commitSummary.value = "Fix: Force upload of index.html and news.html to recover truncated build";
      commitSummary.dispatchEvent(new Event("input", { bubbles: true }));
      commitSummary.dispatchEvent(new Event("change", { bubbles: true }));
      console.log("Commit summary filled.");
    } else {
      console.warn("Commit summary input not found!");
    }

    // Ensure we are selecting the right branch radio option, standard is "Commit directly to the main branch"
    const directRadio = document.querySelector('input[type="radio"][value="direct"]');
    if (directRadio && !directRadio.checked) {
      directRadio.click();
      console.log("Checked direct commit radio.");
    }

    const submitButton = Array.from(document.querySelectorAll('button[type="submit"]')).find(
      b => b.textContent.includes("提交更改") || b.textContent.includes("Commit changes")
    );

    if (submitButton) {
      console.log("Clicking submit button...");
      submitButton.click();
      return "SUCCESS";
    } else {
      console.error("Submit button not found!");
      return "ERROR: Submit button not found";
    }
  } catch (err) {
    console.error(err);
    return "ERROR: " + err.message;
  }
})();
