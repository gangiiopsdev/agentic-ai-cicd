from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = quote(host, safe=':/')
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}