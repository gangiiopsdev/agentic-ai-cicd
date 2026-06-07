from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}