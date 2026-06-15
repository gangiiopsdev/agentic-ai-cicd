from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    command_parts = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    try:
        return ping_host(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}