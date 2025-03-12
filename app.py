from flask import Flask, render_template, request, jsonify
import spacy
import os
import re  # Import regex for custom entity detection

app = Flask(__name__)

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_sm")

def classify_custom_entities(entities):
    """
    Function to classify phone numbers and emails correctly.
    """
    for entity in entities:
        if re.match(r'\+?\d{10,}', entity["text"]):  # Detect phone numbers
            entity["label"] = "PHONE_NUMBER"
        elif re.match(r'\S+@\S+\.\S+', entity["text"]):  # Detect emails
            entity["label"] = "EMAIL"
    return entities

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

    # Apply custom classification for phone numbers and emails
    entities = classify_custom_entities(entities)

    return jsonify({"entities": entities})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

