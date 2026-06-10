from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}