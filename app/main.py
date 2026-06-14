from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}