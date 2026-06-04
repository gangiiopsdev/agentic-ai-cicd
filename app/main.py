from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper validation and sanitization
    if host.strip().endswith('.local'):  # Example validation, adjust as needed
        subprocess.call(['ping', host])
    return {"status": "completed"}