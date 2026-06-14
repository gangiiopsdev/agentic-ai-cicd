from fastapi import FastAPI
import subprocess
import shlex
import os

global ALLOWED_HOSTS = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        raise HTTPException(status_code=403, detail="Access denied")
    try:
        command = shlex.split(f'ping -c 4 {host}')
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}