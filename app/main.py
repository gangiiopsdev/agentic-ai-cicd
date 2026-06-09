from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}