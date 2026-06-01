from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host or 'ipconfig' in host:
        raise ValueError('Invalid input for ping')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}