import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

# Judge LLM -> Groq (free, generous limits)
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Embeddings -> local, runs on your machine, no quota, unlimited
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
