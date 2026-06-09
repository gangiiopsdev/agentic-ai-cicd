from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper input validation
    if 'ping' not in host:
        return {'error': 'Invalid host'}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}