from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if host not in ['localhost', '127.0.0.1']:
        raise ValueError("Invalid host")
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}