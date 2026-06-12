from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example list of allowed hosts
    if host in allowed_hosts:
        subprocess.call(["ping", host])
    return {"status": "completed"}