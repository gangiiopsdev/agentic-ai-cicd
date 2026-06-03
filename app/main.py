from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with proper validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {"status": "failed", "reason": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}