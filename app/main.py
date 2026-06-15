from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and escaping
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')  # Use shlex.quote to escape the input
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
    return {'status': 'completed'}