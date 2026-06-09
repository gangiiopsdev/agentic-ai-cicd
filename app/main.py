from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}