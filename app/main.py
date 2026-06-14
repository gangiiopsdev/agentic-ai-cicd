from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if not host.strip():
        raise ValueError('Host parameter is required and cannot be empty')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}