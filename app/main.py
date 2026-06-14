from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with additional validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'error', 'message': result.stderr}
    return {'status': 'completed'}