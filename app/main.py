from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)