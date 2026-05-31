from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    subprocess.call(['ping', host])
    return {"status": "completed"}