from fastapi import FastAPI
import subprocess
import shlex

gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host or not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    args = shlex.split(f'ping {shlex.quote(host)}')
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}