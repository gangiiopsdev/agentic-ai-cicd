from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum() or len(host) > 50:
        raise ValueError('Invalid host provided')
    subprocess.call(['ping', host])
    return {"status": "completed"}