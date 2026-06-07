from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError("Invalid hostname")
    safe_ping(host)
    return {"status": "completed"}