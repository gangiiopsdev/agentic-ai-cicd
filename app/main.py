from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not host or ' ' in host:
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host or ' ' in host:
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}