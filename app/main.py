from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    command = ["ping", host]
    subprocess.call(command)
    return {"status": "completed"}