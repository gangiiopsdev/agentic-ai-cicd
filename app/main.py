from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.strip() or not all(c.isalnum() for c in host):
        return {"status": "error", "message": "Invalid host"}
    command = ["ping", host]
    subprocess.call(command)
    return {"status": "completed"}