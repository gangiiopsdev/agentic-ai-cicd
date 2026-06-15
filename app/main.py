from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = quote_plus(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}