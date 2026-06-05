from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}