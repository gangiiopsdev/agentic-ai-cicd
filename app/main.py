from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isdigit():
        raise ValueError('Invalid host')
    return f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = safe_ping(host)
    subprocess.call(command, shell=False)
    return {"status": "completed"}