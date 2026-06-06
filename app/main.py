from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host or not host.strip().isalnum():
        raise ValueError("Invalid host input")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}