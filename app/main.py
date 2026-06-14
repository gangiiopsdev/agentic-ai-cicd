from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if host.strip() == 'localhost' or host.startswith('192.168.1.'):
        subprocess.run(['ping', host], check=True)
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}