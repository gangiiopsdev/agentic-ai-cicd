from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}