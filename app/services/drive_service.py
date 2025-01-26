from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
import os
import logging
from PyPDF2 import PdfReader


FOLDER_ID = "1MGhZL4PJ5uDcjayMBbbfKBkln5XX5zkl"
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

logging.basicConfig(level=logging.DEBUG)

def preprocess_documents(raw_data_path):
    logging.info("Avvio del preprocessing dei documenti...")
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    for filename in os.listdir(raw_data_path):
        if filename.endswith(".pdf"):
            logging.info(f"Elaborando: {filename}")
            reader = PdfReader(os.path.join(raw_data_path, filename))
            text = " ".join([page.extract_text() for page in reader.pages])
            output_file = os.path.join(PROCESSED_DATA_PATH, filename + ".txt")
            with open(output_file, "w") as f:
                f.write(text)
            logging.info(f"Salvato il testo preprocessato in: {output_file}")

