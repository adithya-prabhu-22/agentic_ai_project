import os
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="rag/vector_store",
    embedding_function=embeddings
)

retriever = vectordb.as_retriever(search_kwargs={"k": 5})

llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"   # ✅ Updated model
)

prompt_template = """
You are a tax assistant.

STRICT RULES:
1. Answer ONLY using the provided context.
2. Do NOT use external knowledge.
3. If the answer is not in the context, say "Information not available in provided documents."
4. Do NOT assume or calculate anything not explicitly mentioned.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate.from_template(prompt_template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

def query_tax_regime(question: str):
    return rag_chain.invoke(question)

if __name__ == "__main__":
    test_questions = [
        "What are the tax slabs in new regime for FY 2025-26?",
        "What is Section 87A rebate amount?",
        "Compare old and new tax regimes",
    ]

    for q in test_questions:
        print(f"\nQ: {q}")
        print("A:", query_tax_regime(q))
        print("-" * 80)