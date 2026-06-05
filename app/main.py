from fastapi import FastAPI
import subprocess
import shlex
global_ping = "ping -c 1"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = f'{global_ping} {host}'
    args = shlex.split(command)
    subprocess.call(args)
    return {"status": "completed"}