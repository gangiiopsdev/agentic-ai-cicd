from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate input
    if not host or not host.strip():
        raise ValueError("Invalid host input")
    subprocess.call(["ping", host])
    return {"status": "completed"}