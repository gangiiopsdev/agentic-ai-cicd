from fastapi import FastAPI
import subprocess
import shlex
from typing import Union

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(e for e in input_str if e.isalnum() or e in '.-')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError('Invalid host provided')
    command = ['ping', *shlex.split(sanitized_host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}