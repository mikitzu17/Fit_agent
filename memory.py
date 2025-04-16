from langchain.vectorstores import SupabaseVectorStore
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from supabase import create_client
import os

def get_vectorstore():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_API_KEY")
    client = create_client(url, key)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    vectorstore = SupabaseVectorStore(client=client, embedding=embeddings, table_name="chat_memory")
    return vectorstore
