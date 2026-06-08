from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid host input")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}