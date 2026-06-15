from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(shlex.split(f'ping {host}'), check=True, shell=False)
    return {"status": "completed"}