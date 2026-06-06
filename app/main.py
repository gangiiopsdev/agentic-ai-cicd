from fastapi import FastAPI
import subprocess
import shlex

global_host = '127.0.0.1'  # Replace with safe default value

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        host = global_host
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}