from fastapi import FastAPI
import subprocess
import re

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

def execute_ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    safe_host = subprocess.quote(host)
    try:
        output = subprocess.check_output(['ping', '-c 1', '--'] + [safe_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_ping(subprocess.quote(host))