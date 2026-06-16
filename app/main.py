from fastapi import FastAPI
import subprocess
from shlex import quote
cimport re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host parameter")
    subprocess.call(["ping", quote(host)])
    return {"status": "completed"}