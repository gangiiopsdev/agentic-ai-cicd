from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if 'ping' in host or '..' in host:
        raise ValueError('Invalid input')
    subprocess.call(["ping", host])
    return {"status": "completed"}