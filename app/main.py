from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if host not in ['example.com', '127.0.0.1']:
        raise ValueError('Invalid host')
    subprocess.call(["ping", host])
    return {"status": "completed"}