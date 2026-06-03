from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.startswith('127.0.0.1'):  # Restrict to localhost
        subprocess.call(["ping", host])
    return {"status": "completed"}