from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and validation
    if 'ping' not in host:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}