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
        result = subprocess.run(args, check=True, shell=shell, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ['8.8.8.8', '127.0.0.1']:
        return {'status': 'error', 'message': 'Invalid host'}
    command = f'ping {host}'
    result = execute_command(command, shell=False)
    if isinstance(result, dict):
        return result
    else:
        return {'status': 'completed', 'output': result}