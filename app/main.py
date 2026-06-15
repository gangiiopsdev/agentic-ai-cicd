from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    cmd = shlex.split('ping ' + shlex.quote(host))
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)