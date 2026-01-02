import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

documents = []

for folder in ["data/resumes", "data/jobs"]:
    for file in os.listdir(folder):
        loader = TextLoader(f"{folder}/{file}")
        documents.extend(loader.load())

db = FAISS.from_documents(documents, OpenAIEmbeddings())
db.save_local("vector_store")

print("✅ Resume + job documents indexed")
