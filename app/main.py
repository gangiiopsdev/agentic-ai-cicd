from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return safe_ping(host)