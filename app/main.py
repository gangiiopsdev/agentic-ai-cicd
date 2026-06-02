from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_hostname(host):
    if not host or not all(c.isalnum() or c in '-.' for c in host):
        return None
    return host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_hostname(host)
    if sanitized_host is None:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    args = shlex.split(f'ping {sanitized_host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}