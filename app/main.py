from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError("Invalid input")
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}