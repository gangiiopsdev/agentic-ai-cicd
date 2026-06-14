from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with validation
    safe_host = host.strip().replace(' ', '_')
    if not safe_host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}