from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Improved implementation using shlex.split to safely handle command arguments
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {"status": "completed"}