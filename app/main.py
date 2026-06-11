from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input):
    return ''.join(c for c in input if c.isalnum() or c.isdigit() or c in '.-')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed'}