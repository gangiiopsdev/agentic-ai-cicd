from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    if not valid_host(host):
        raise ValueError('Invalid host')
    command = ['ping', host]
    subprocess.run(command, check=True)

def valid_host(host):
    return bool(re.match(r'^[a-zA-Z0-9-._]+$', host))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}