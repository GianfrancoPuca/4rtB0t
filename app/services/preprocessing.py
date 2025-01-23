import os
from PyPDF2 import PdfReader

PROCESSED_DATA_PATH = "data/processed/"

def preprocess_documents(raw_data_path):
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    for filename in os.listdir(raw_data_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(raw_data_path, filename))
            text = " ".join([page.extract_text() for page in reader.pages])
            with open(os.path.join(PROCESSED_DATA_PATH, filename + ".txt"), "w") as f:
                f.write(text)
