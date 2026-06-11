from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {'status': 'completed'}