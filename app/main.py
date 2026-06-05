from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if not host.isalnum():
        raise ValueError("Invalid host name")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}