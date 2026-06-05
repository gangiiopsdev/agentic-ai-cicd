from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    command = shlex.split(f'ping {host}')
    output = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}