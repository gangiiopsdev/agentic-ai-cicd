from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is not None:
        subprocess.call(["ping", host])
    return {"status": "completed"}