from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum())

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    return any(host.endswith(suffix) for suffix in allowed_hosts)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}