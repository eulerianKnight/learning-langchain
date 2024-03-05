from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
load_dotenv()

# Chunking Text
text_splitter = CharacterTextSplitter(
    separator="\n", 
    chunk_size=200, 
    chunk_overlap=100
)

# Document Loader
loader = TextLoader("facts.txt")
docs = loader.load_and_split(text_splitter=text_splitter)

# # Check how the chunking and loader works
# for doc in docs:
#     print(doc.page_content)
#     print("\n")

# Embeddings
embeddings = OpenAIEmbeddings()

# Vectorstore
# Instantiate ChromaDB Vectorstore
db = Chroma.from_documents(
    docs, 
    embedding=embeddings, 
    persist_directory="emb"
)

results = db.similarity_search_with_score("What is an interesting fact about the english language?")

# # Check the results
# for result in results:
#     print("\n")
#     print(result[1])
#     print(result[0].page_content)