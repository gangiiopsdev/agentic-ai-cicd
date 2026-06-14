from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([quote(host)])
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}