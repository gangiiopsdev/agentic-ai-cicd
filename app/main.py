from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex and avoiding shell=True
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}