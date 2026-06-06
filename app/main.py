from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if any(x in host for x in ['&&', ';', '||']):
        raise ValueError('Invalid characters in host parameter')
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}