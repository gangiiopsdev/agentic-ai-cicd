from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.strip() == host and not host.startswith('-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', *shlex.split(host)], check=True)
    return {'status': 'completed'}