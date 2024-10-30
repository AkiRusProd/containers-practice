from backend.src.llm_agent import LLMAgent
from backend.src.llm import GigaChatLLM
from backend.src.embedder import HFEmbedder
from backend.src.chroma_client import ChromaClient
from fastapi import FastAPI, Body
from typing import List, Optional, Union


llm = GigaChatLLM()
embedder = HFEmbedder()

chroma_client = ChromaClient(
    host='chromadb', port=8000,
    embedder = embedder
)

llm_agent = LLMAgent(llm, chroma_client)
app = FastAPI()

@app.post("/response")
def response(
    prompt: str = Body(default="Hello!", embed=True),
):
    generated_text_response = llm_agent.response(prompt)

    generated_text = generated_text_response

    return generated_text

@app.post("/memory_response")
def memory_response(
    prompt: str = Body(default="Hello!", embed=True),
    collection_name: str = Body(default="default", embed=True),
    n_results: int = Body(default=3, embed=True),
    memory_access_threshold: float = Body(default=1.5, embed=True),
):
    generated_text_response = llm_agent.memory_response(prompt, collection_name, n_results, memory_access_threshold)

    generated_text = generated_text_response

    return generated_text

@app.post("/add_memory")
def add_memory(
    text: str = Body(default=None, embed=True),
    collection_name: str = Body(default="default", embed=True),
):
    chroma_client.add(text, collection_name) if text != "" else None

    return "OK"

@app.post("/delete_memory")
def delete_memory(
    id: str = Body(default=None, embed=True),
    collection_name: str = Body(default="default", embed=True),
):
    chroma_client.delete(id, collection_name) if id != "" else None

    return "OK"

@app.post("/query_memory")
def query_memory(
    query: str = Body(default=None, embed=True),
    n_results: int = Body(default=3, embed=True),
    return_text: bool = Body(default=True, embed=True),
    collection_name: str = Body(default="default", embed=True),
):
    return chroma_client.query(query, n_results, return_text, collection_name)