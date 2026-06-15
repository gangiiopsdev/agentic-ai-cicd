from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}