from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

global_ping = 'ping -c 1'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    command = f'{global_ping} {host}'
    args = shlex.split(command)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}