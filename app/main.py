from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    # Validate input
    if not host.strip() or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return ping(host)