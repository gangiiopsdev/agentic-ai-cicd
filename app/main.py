from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum() or '-' in host:
        return {'status': 'failed', 'error': 'Invalid host input'}
    result = subprocess.run(shlex.split(f'ping {host}'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}