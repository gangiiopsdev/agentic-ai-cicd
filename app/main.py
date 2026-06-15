from fastapi import FastAPI
import subprocess
import shlex
git_hash = 'unknown'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}