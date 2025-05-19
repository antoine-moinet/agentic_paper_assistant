from fastapi import FastAPI
from agent import answer_query

app = FastAPI()

@app.get("/ask")
async def ask_endpoint(q: str):
    return {"answer": answer_query(q)}
