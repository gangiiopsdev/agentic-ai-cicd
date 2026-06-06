from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid input for ping")
    subprocess.call(["ping", host])
    return {"status": "completed"}