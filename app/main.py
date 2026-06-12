from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    else:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}