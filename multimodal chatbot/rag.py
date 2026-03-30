
import os
from dotenv import load_dotenv
from text_converter import extract_text
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="GROQ_API_KEY",
    temperature=0
)

embedding = HuggingFaceEmbeddings()
vectordb = Chroma(
    collection_name="finance",
    embedding_function=embedding
)


vectordb.add_texts([
    "Netflix charges monthly subscription fees",
    "Amazon includes GST tax in purchases",
    "Bank may deduct service charges",
])


def retrieve_context(query):
    docs = vectordb.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in docs])


def explain(question, file_path):
    text = extract_text(file_path)
    context = retrieve_context(question)

    prompt = f"""   
    Document:
    {text} 

    Context:
    {context}

    Question:
    {question}

    Explain the charges clearly.
    """

    return llm.invoke(prompt).content