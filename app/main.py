from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    valid_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host in valid_hosts:
        command = f'ping {host}'
        args = shlex.split(command)
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)