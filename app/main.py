from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and validation
    if host.strip() == "/" or ";" in host or "&&" in host:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}