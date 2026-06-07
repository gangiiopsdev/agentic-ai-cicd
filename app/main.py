from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a whitelist of allowed hosts
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}