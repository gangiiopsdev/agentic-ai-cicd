from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    # Simple regex for alphanumeric characters
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isalnum():
        return {'error': 'Invalid hostname'}
    subprocess.call(shlex.split(f'ping {sanitized_host}'))
    return {'status': 'completed'}