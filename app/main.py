from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and escaping
    if not host.isalnum() or len(host) > 255:
        return {"status": "failed", "reason": "Invalid host name"}
    subprocess.call(["ping", host])
    return {"status": "completed"}