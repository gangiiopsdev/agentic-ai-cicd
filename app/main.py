from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None or not isinstance(host, str) or not host.strip():
        return {"status": "failed", "error": "Invalid input"}

    try:
        subprocess.run(["ping", host], check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}