from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
def execute_command(command: str, shell=False):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
def safe_execute_command(host: str):
    if host not in ['8.8.8.8', '127.0.0.1']:
        raise ValueError('Invalid host')
    command = f'ping {host}'
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_execute_command(host)
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}