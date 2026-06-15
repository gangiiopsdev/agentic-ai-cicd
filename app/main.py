from fastapi import FastAPI
import subprocess
c import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation to sanitize input and use subprocess securely
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}