from fastapi import FastAPI
import subprocess
import shlex
from typing import Union

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(filter(lambda x: x.isalnum() or x in ' .', input_str))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        command = ['ping'] + shlex.split(sanitized_host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}