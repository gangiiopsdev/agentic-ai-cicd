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
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}