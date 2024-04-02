# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain_community.document_loaders import DirectoryLoader
# from langchain_community.vectorstores import FAISS
# from PyPDF2 import PdfReader
from pathlib import Path
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

response = supabase.table('knowledge').select("*").execute()

for resp in response.data:
    print(resp["label"])