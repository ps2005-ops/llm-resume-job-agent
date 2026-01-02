from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

db = FAISS.load_local(
    "vector_store",
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True
)

def retrieve(query: str, k: int = 4):
    return db.similarity_search(query, k=k)
