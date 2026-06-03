from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with proper security checks
    if host.startswith('192.168.1.'):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")