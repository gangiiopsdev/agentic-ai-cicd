from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Sanitize input to prevent shell injection
    if any(char in host for char in [';', '&', '|', '(', ')', '$']):
        raise ValueError('Invalid input')
    command = ['ping', f'-c 1 {shlex.quote(host)}']
    subprocess.run(command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping/')
def ping_host(host: str):
    # Sanitize input to prevent shell injection
    if any(char in host for char in [';', '&', '|', '(', ')', '$']):
        raise ValueError('Invalid input')
    command = ['ping', f'-c 1 {shlex.quote(host)}']
    subprocess.run(command, check=True)
    return {'status': 'completed'}