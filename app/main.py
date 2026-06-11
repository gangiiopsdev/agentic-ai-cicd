from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or not host.isalnum():
        raise ValueError("Invalid host name")
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}