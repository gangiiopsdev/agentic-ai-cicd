from fastapi import FastAPI
import subprocess
import shlex
import re

global_regex = re.compile(r'^[a-zA-Z0-9.-]+$')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not global_regex.match(host):
        raise ValueError('Invalid input for ping command')
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}