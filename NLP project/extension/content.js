chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extract_text") {
        sendResponse({ text: document.body.innerText });
    }
});
