from flask import Blueprint, request, jsonify, render_template
from app.services.llm_service import preprocess_documents, load_documents, prepare_documents, get_answer
import logging

main = Blueprint("main", __name__)
logging.basicConfig(level=logging.DEBUG)

# Rotta per la pagina principale (index.html)
@main.route("/")
def home():
    return render_template("index.html")

# Preprocessa i documenti caricati
@main.route("/api/preprocess", methods=["POST"])
def preprocess():
    preprocess_documents("data/raw/")
    return jsonify({"message": "Documenti preprocessati con successo."})

# Ottieni una risposta basata sui documenti e Ollama
@main.route("/api/query", methods=["POST"])
def query():
    question = request.json.get("question")
    documents = load_documents()
    db = prepare_documents(documents)
    answer = get_answer(question, db)
    return jsonify({"answer": answer})

@main.route("/api/feedback", methods=["POST"])
def feedback():
    data = request.json
    question = data.get("question")
    feedback_value = data.get("feedback")
    # Qui decidi come salvare il feedback, es. su un DB
    return jsonify({"success": True, "message": "Feedback received"})

