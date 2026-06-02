from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def run_safe_command(command: str):
    if not any(os.path.basename(cmd) == 'ping' for cmd in command.split()):
        raise ValueError('Command not allowed')
    args = shlex.split(command)
    subprocess.call(args, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = f'ping {host}'
    run_safe_command(command)
    return {'status': 'completed'}