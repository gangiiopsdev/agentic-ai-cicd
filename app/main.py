from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isnumeric() or len(host) > 3:
        raise ValueError('Invalid hostname provided')
    args = shlex.split(f'ping {host}')
    subprocess.run(args)
    return {'status': 'completed'}