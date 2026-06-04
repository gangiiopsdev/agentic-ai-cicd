from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.strip() or host.strip().isalnum():
        subprocess.call(["ping", host])
    else:
        raise ValueError('Invalid host parameter')

    return {"status": "completed"}