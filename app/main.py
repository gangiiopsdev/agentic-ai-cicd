from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if 'localhost' not in host and '127.0.0.1' not in host:
        return {'error': 'Invalid host'}
    subprocess.call(["ping", host])
    return {"status": "completed"}