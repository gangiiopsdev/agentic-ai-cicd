from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with command validation and sanitization
    if host.startswith('192.168.') or host.startswith('localhost'):
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {"status": "completed"}
    else:
        return {"status": "Invalid host"}