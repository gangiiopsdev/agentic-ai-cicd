from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent shell injection
    if 'ping' in host:
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if 'ping' in host:
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}