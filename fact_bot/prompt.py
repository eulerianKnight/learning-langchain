from dotenv import load_dotenv

import langchain
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

from redundant_filter_retriever import RedundantFilterRetriever

langchain.debug = True

load_dotenv()

# Embeddings
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb", 
    embedding_function=embeddings
)

# Retrieval Chain
# Create Retriever
retriever = RedundantFilterRetriever(
    embeddings=embeddings, 
    chroma=db
)
# Instantitate ChatModels
chat = ChatOpenAI()
chain = RetrievalQA.from_chain_type(
    llm=chat, 
    retriever=retriever, 
    chain_type="stuff"
)

result = chain.invoke("What is an interesting fact about the English Language?")

print(result['result'])
