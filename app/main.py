from fastapi import FastAPI
import subprocess
from typing import List
import shlex

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts

def validate_host(host: str) -> bool:
    return host in allowed_hosts

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)