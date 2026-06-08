from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}