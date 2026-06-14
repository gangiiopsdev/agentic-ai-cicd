from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum():
        return {"error": "Invalid hostname"}
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}