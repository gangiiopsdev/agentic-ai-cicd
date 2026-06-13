from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    return {'status': 'completed'}