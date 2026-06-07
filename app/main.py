from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = shlex.split(f'ping {sanitized_host}')
    subprocess.call(command_parts)
    return {'status': 'completed'}