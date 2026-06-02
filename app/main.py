from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError('Invalid hostname')
    return ''.join(c for c in input_str if c.isalnum())

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {'status': 'completed'}