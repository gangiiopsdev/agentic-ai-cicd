from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

def run_ping(host):
    command_parts = ['ping', sanitized_host]
    result = subprocess.run(command_parts, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return run_ping(sanitized_host)