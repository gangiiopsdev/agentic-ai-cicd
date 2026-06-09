from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host and '@' not in host:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host input"}