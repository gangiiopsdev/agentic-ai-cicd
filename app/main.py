from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

def ping(host: str):
    validate_host(host)
    try:
        # Use shlex to safely quote command arguments
        subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    return ping(host)