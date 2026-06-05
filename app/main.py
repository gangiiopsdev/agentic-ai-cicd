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
    if not host.isalnum() or ' ' in host:
        raise ValueError("Invalid host name")
    subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True)
    return {"status": "completed"}