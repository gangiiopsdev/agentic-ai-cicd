from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(host):
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid input')
    return host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}