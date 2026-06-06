from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or not host.strip():
        raise ValueError("Invalid host provided")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}