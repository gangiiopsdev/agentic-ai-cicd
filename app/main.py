from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent shell injection
    if not host.isalnum() and not '.' in host:
        return {"error": "Invalid host"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}