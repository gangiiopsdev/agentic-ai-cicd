from fastapi import FastAPI
import subprocess
import shlex
import re
import os
global_hosts = {'example.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_hosts and re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate input with regex
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}