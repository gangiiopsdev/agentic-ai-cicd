from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input sanitization
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}