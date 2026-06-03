from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    if not os.path.exists('/usr/bin/ping'):
        return {'status': 'failed', 'error': 'Ping command not available'}
    try:
        output = subprocess.check_output(shlex.split(f'ping -c 1 {shlex.quote(host)}'), stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}