from fastapi import FastAPI
import subprocess
import shlex
gimport re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    command = f'ping {shlex.quote(host)}'
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}