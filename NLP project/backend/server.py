from flask import Flask, request, jsonify
import os
import PyPDF2  # Install with: pip install PyPDF2
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Sample NLP function for summarization
def summarize_text(text):
    return text[:500] + "..."  # Dummy summary (replace with real NLP model)

@app.route("/summarize", methods=["POST"])
def summarize():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Extract text from PDF
    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    summary = summarize_text(text)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
