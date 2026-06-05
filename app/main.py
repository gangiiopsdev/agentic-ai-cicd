from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with input sanitization
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    subprocess.call(shlex.split(f'ping {host}'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input sanitization
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}