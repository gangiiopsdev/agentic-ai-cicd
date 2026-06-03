from fastapi import FastAPI
import subprocess

app = FastAPI()
global_hosts = {'example.com'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_hosts:
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize input
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}