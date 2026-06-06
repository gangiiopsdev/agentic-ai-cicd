from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping'] + shlex.split('-- ' + host)
    subprocess.call(args, shell=False)
    return {'status': 'completed'}