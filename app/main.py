from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/{path:path}")
def home(path: str):
    return {"message": f"Agentic Self-Healing Pipeline at {path}"}