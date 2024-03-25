import os
from pinecone import Pinecone as pinecone_client
from langchain_pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

pinecone_client(
    api_key=os.getenv("PINECONE_API_KEY"), 
    environment=os.getenv("us-west-2")
)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), 
    embeddings
)