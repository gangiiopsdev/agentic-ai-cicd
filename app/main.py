from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)