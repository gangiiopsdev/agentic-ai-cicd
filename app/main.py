from fastapi import FastAPI
import subprocess
import shlex
global_hosts = {'example.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_hosts:
        command = ['ping', host]
        subprocess.call(command)
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}