from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host input')
    args = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.call(args, shell=False)
    return {'status': 'completed'}