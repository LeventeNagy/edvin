from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Knowledge():

    def licensing():
        
        label = ""
        data = ""

        results = supabase.table('knowledge').select("*").execute()
        
        for result in results.data:
            label += result["label"]
            data += result["info"]
        
        return label, data