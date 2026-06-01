from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation with sanitization
    if not host.strip() or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host parameter')
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}