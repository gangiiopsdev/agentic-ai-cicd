from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host or host.strip() == '':
        raise ValueError('Host parameter is required and cannot be empty')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {"status": "completed"}