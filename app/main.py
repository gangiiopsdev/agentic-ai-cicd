from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a valid hostname or IP address
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host format')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}