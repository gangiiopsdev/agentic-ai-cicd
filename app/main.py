from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Validate the host input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host format')

    args = shlex.split(f'ping {host}')
    output = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return result
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}