document.getElementById("uploadBtn").addEventListener("click", async () => {
    let fileInput = document.getElementById("fileInput");
    
    if (fileInput.files.length === 0) {
        alert("Please select a PDF file.");
        return;
    }

    let file = fileInput.files[0];
    let formData = new FormData();
    formData.append("file", file);

    try {
        let response = await fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            body: formData
        });

        let data = await response.json();
        document.getElementById("result").innerText = data.summary;
    } catch (error) {
        console.error("Error uploading file:", error);
        alert("Failed to upload. Make sure the Flask server is running.");
    }
});
