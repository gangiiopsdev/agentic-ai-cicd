from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation with validation
    if not host.strip().isalnum() or len(host.split('.')) != 4:
        raise ValueError("Invalid host name")
    subprocess.call(["ping", host])
    return {"status": "completed"}