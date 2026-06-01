from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper sanitization
    if host and all(c.isalnum() or c in '.-' for c in host):  # Basic validation
        subprocess.call(["ping", host])
    return {"status": "completed"}