
from src.llm import GigaChatLLM

from fastapi import FastAPI, Body
from typing import List, Optional, Union


llm = GigaChatLLM()
app = FastAPI()

@app.post("/response")
def response(
    prompt: str = Body(default="Hello!", embed=True),
):
    generated_text_response = llm.response(prompt)

    generated_text = generated_text_response

    return generated_text







