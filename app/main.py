from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}