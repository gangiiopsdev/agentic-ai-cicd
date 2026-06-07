from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: Optional[str] = None):
    if host is None:
        return {'status': 'failed', 'error': 'No host provided'}
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.check_output(args, timeout=10, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}