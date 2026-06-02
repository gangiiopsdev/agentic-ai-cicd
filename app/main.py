from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    return subprocess.run(['ping', quote(host)], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {"status": "completed"}