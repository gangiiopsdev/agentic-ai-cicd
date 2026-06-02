from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if not host.isalnum() and '-' not in host:
        return {'error': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}