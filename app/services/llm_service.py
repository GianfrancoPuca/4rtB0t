import logging
import os
import numpy as np
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from transformers import AutoTokenizer
import ollama
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

PROCESSED_DATA_PATH = "data/processed/"

# Inizializza il tokenizer Transformers
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def get_tokenizer_embeddings(texts):
    """Crea rappresentazioni numeriche dei testi usando il tokenizer."""
    embeddings = []
    for text in texts:
        tokens = tokenizer.encode(text, truncation=True, max_length=512)
        embedding = np.array(tokens, dtype=np.float32) / np.linalg.norm(tokens)
        embeddings.append(embedding)
    return embeddings


def preprocess_documents(raw_data_path):
    """Preprocessa i documenti PDF e li salva come testo."""
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    for filename in os.listdir(raw_data_path):
        if filename.endswith(".pdf"):
            logger.info(f"Elaborando: {filename}")
            reader = PdfReader(os.path.join(raw_data_path, filename))
            text = " ".join([page.extract_text() for page in reader.pages])
            output_file = os.path.join(PROCESSED_DATA_PATH, filename + ".txt")
            with open(output_file, "w") as f:
                f.write(text)
            logger.info(f"Salvato il testo preprocessato in: {output_file}")

def load_documents():
    """Carica i documenti preprocessati."""
    logger.info("Caricamento dei documenti preprocessati...")
    documents = []
    for filename in os.listdir(PROCESSED_DATA_PATH):
        if filename.endswith(".txt"):
            with open(os.path.join(PROCESSED_DATA_PATH, filename), "r") as f:
                documents.append({"content": f.read(), "source": filename})
    logger.info(f"Caricati {len(documents)} documenti.")
    return documents

def prepare_documents(documents):
    logger.info("Preparazione dei documenti per embedding...")

    # Suddivisione dei documenti
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.create_documents(
        [doc["content"] for doc in documents],
        metadatas=[{"source": doc["source"]} for doc in documents]
    )

    # Estrai i contenuti di testo e le relative metadati
    text_contents = [doc.page_content for doc in docs]
    metadatas = [doc.metadata for doc in docs]

    # Inizializza il modello di embedding
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    try:
        # Crea l’indice FAISS usando i testi e il modello di embedding
        db = FAISS.from_texts(text_contents, embedding_model, metadatas=metadatas)
        logger.info("Documenti preparati e indicizzati con successo.")
        return db
    except Exception as e:
        logger.error(f"Errore durante la creazione dell'indice FAISS: {e}")
        raise


def query_ollama(question, context, sources):
    """Interroga il modello Ollama."""
    try:
        response = ollama.chat(model='gemma2:2b', messages=[
            {"role": "system", "content": "Sei un assistente specializzato in mostre d'arte. Rispondi sempre in modo conciso. Rispondi sempre in italiano alle domande degli utenti."},
            {"role": "user", "content": f"Contesto: {context}\n\nFonti: {sources}\n\nDomanda: {question}"}
        ])
        return response['message']['content']
    except Exception as e:
        logger.error(f"Errore nella comunicazione con Ollama: {e}")
        return "Errore nella comunicazione con il modello Ollama."

def get_answer(question, db):
    """Trova una risposta alla domanda utilizzando Ollama e i documenti preprocessati."""
    docs = db.similarity_search(question, k=3)
    context = " ".join([doc.page_content for doc in docs])
    sources = ", ".join(set([doc.metadata['source'] for doc in docs]))
    return query_ollama(question, context, sources)
