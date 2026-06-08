from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if host in ['127.0.0.1', 'localhost']:
        subprocess.run(['ping', host], check=True)
    return {"status": "completed"}