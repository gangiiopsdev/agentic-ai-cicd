from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not urlparse(host).netloc:
        return {"error": "Invalid host"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}