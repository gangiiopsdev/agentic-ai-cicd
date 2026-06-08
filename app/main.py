from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric() and '-' not in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)