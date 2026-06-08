from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', ':', '-', '_', '/'))

app = FastAPI()
global_ping = 'ping -c 1'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'{global_ping} {sanitized_host}'
    args = shlex.split(command)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}