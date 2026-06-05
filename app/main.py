from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with args parameter and validation
    if host.startswith('.'):
        return {'status': 'Invalid host'}
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with args parameter and validation
    if host.startswith('.'):
        return {'status': 'Invalid host'}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}