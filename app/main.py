from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.call with sanitized input
    if host in ['google.com', 'example.com']:  # Example allowed hosts
        subprocess.call(["ping", host])
    else:
        raise ValueError('Invalid host')

    return {"status": "completed"}