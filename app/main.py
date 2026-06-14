from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.strip() or len(host.split()) > 1:
        raise ValueError("Invalid host input")
    subprocess.call(["ping", host])
    return {"status": "completed"}