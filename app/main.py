from fastapi import FastAPI
import subprocess
import os

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if len(sanitized_host) != len(host):
        raise ValueError('Invalid input')
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}