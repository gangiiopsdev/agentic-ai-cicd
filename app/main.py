from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum():
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum():
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}