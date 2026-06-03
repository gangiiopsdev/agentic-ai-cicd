from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid host name")
    # Use a safer method with shell=False
    subprocess.run(["ping", host], check=True, text=True, capture_output=True)
    return {"status": "completed"}