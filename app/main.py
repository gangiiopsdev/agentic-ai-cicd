from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

allowed_hosts: List[str] = ['example.com', 'test.com']  # Define a list of allowed hosts

def validate_host(host: str):
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}