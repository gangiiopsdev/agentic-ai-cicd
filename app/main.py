from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.strip() == host and not host.startswith('-')

def safe_ping(host: str) -> dict:
    if not validate_host(host):
        raise ValueError('Invalid host name')
    try:
        subprocess.run(['ping', *shlex.split(host)], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)