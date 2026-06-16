from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/{path:path}")
def home(path: str):
    safe_path = os.path.abspath(path)
    return {"message": f'Agentic Self-Healing Pipeline at {safe_path}'}