from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}