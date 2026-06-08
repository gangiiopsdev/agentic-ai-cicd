from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}