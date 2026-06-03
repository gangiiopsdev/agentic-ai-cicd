from fastapi import FastAPI
import subprocess
from html import escape

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    if not host.isalnum():
        raise ValueError("Invalid host name")
    sanitized_host = escape(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)
    return {"status": "completed"}