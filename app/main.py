from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Input validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid input for host')
    subprocess.call(['ping', host])
    return {'status': 'completed'}