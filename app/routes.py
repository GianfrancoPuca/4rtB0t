from flask import Blueprint, request, jsonify
from app.services.drive_service import fetch_documents
from app.services.llm_service import generate_response

main = Blueprint("main", __name__)

@main.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = generate_response(user_message)
    return jsonify({"response": response})

@main.route("/api/load-docs", methods=["GET"])
def load_docs():
    documents = fetch_documents()
    return jsonify({"documents_loaded": len(documents)})
