from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError("Invalid host name")
    result = subprocess.call(["ping", quote(host)])
    return {"status": "completed", "result": result}