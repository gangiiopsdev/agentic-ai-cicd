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
    if not host or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid input'}
    command = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}