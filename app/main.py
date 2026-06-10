from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input before using it in the subprocess call
    if 'ping' not in host or '.' not in host:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}