from flask import Flask, render_template, request, jsonify
import spacy
import os
import re  # Import regex for custom entity detection

app = Flask(__name__)

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_sm")

def mask_sensitive_info(text):
    """
    Function to mask phone numbers, emails, and URLs in the input text.
    """
    # Mask phone numbers (10+ digits)
    text = re.sub(r'\b\d{10,}\b', 'xxxxxxxxxx', text)

    # Mask emails
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'xxxxxxxx@xxxxx.com', text)

    # Mask URLs
    text = re.sub(r'\bhttps?://\S+\b', 'xxxxx', text)

    return text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ner", methods=["POST"])
def ner():
    data = request.json
    text = data.get("text", "")

    # Extract named entities
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Mask sensitive information
    masked_text = mask_sensitive_info(text)

    return jsonify({"masked_text": masked_text, "entities": entities})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


