from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host parameter")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}