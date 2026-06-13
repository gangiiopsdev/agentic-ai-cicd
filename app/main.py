from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    result = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "result": result.stdout,
        "returncode": result.returncode
    }