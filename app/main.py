from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add validation logic here to ensure host is safe
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        subprocess.run(['ping', f'"{sanitized_host}"'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}