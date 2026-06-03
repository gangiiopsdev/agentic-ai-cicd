from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    return subprocess.call(args, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host format")
    result = safe_ping(host)
    return {"status": "completed", "result": result}