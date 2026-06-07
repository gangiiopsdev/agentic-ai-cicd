from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 64:
        return {"status": "failed", "reason": "Invalid host name"}
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}