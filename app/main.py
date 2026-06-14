from fastapi import FastAPI
import subprocess
cimport shlex
global ping_command = shlex.split(f'ping {host}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(ping_command)

    return {"status": "completed"}