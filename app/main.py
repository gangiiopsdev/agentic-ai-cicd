from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

allowed_hosts = set(['example.com', 'test.com'])

def ping(host: str):
    # Secure implementation with validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid or unallowed host'}
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)