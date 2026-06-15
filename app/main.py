from fastapi import FastAPI
import subprocess
import shlex
global_hosts = {'example.com', 'localhost'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in global_hosts:
        raise ValueError('Invalid host')
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}