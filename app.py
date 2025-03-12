from flask import Flask, render_template, request, jsonify
import spacy
import subprocess

app = Flask(__name__)

# Ensure the model is installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ner", methods=["POST"])
def ner():
    data = request.json
    text = data.get("text", "")

    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    return jsonify({"entities": entities})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

