(async () => {
  const textarea = document.querySelector('textarea.cm-content') || document.querySelector('.cm-content') || document.querySelector('textarea[name="value"]');
  if (textarea) {
    if (textarea.tagName === 'TEXTAREA') {
      textarea.value = `LOCAL_CONTENT_PLACEHOLDER`;
      textarea.dispatchEvent(new Event('input', { bubbles: true }));
      textarea.dispatchEvent(new Event('change', { bubbles: true }));
    } else if (textarea.classList.contains('cm-content')) {
        // CodeMirror 6
        const view = textarea.parentElement.parentElement.parentElement.CodeMirror || textarea.parentElement.parentElement.parentElement.view;
        // This is tricky. Let's try the simpler way first: set textContent and dispatch events.
        textarea.textContent = `LOCAL_CONTENT_PLACEHOLDER`;
        textarea.dispatchEvent(new Event('input', { bubbles: true }));
    }
  } else {
    // Fallback: try to find any textarea that might be the editor
    const allTextareas = Array.from(document.querySelectorAll('textarea'));
    const editor = allTextareas.find(t => t.getAttribute('aria-label')?.includes('Editing') || t.name === 'value');
    if (editor) {
      editor.value = `LOCAL_CONTENT_PLACEHOLDER`;
      editor.dispatchEvent(new Event('input', { bubbles: true }));
    }
  }
})()
