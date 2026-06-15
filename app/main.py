from fastapi import FastAPI
import subprocess
import re

global allow_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if host not in allow_hosts:
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}