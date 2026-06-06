from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    return host.replace('@', '').replace('.', '').replace('-', '')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping'] + shlex.split(sanitized_host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}