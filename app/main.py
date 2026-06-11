from fastapi import FastAPI
import subprocess
import shlex
def run_safe_ping(host):
    if not host.strip():
        raise ValueError('Invalid input for host parameter')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return run_safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}