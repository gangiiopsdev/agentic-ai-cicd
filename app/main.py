from fastapi import FastAPI
import subprocess
import shlex
import os

current_user = os.getlogin()
if current_user != 'root':
    raise Exception('Only root can execute this command')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}