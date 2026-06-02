from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}