from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host not in ('127.0.0.1', '::1', 'localhost'):
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', '4', host], check=True)
    return {"status": "completed"}