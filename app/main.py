from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')

    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}