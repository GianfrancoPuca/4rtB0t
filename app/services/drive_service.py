from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
import os

FOLDER_ID = "1MGhZL4PJ5uDcjayMBbbfKBkln5XX5zkl"
RAW_DATA_PATH = "data/raw/"

def fetch_documents():
    credentials = Credentials.from_service_account_file("config/secrets.json")
    service = build("drive", "v3", credentials=credentials)
    query = f"'{FOLDER_ID}' in parents and mimeType='application/pdf'"

    results = service.files().list(q=query).execute()
    files = results.get("files", [])

    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    for file in files:
        request = service.files().get_media(fileId=file["id"])
        filepath = os.path.join(RAW_DATA_PATH, file["name"])
        with open(filepath, "wb") as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()
    return files
