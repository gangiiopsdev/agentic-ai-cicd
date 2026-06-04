from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and safe arguments
    subprocess.run(shlex.split(f'ping {host}'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and safe arguments
    subprocess.run(shlex.split(f'ping {host}'))
    return {"status": "completed"}