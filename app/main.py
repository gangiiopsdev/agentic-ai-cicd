from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.strip().isdigit():
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'result': response}