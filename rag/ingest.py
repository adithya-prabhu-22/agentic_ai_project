import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

def ingest_documents():
    file_path = "data/pdfs/tax_regime_summary_2025.txt"

    if not os.path.exists(file_path):
        print(f"ERROR: File not found at {os.path.abspath(file_path)}")
        return

    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="rag/vector_store"
    )

    vectordb.persist()

    print(f"Successfully ingested {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")
    print("Vector store saved at: rag/vector_store")


if __name__ == "__main__":
    ingest_documents()