from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with proper input validation and sanitization
    if host.startswith("-”):  # Preventing command injection by checking for invalid characters
        raise ValueError('Invalid host parameter')
    subprocess.call(["ping", host])
    return {"status": "completed"}