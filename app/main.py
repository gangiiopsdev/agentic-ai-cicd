from fastapi import FastAPI
import subprocess
import shlex
global_host = 'example.com'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host == global_host:
        subprocess.run(shlex.split(f'ping {host}'), check=True)
    else:
        return {'error': 'Unauthorized access attempt'}
    return {'status': 'completed'}