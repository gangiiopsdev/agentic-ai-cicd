from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.isalnum() and '.' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid hostname'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True, text=True)
    return {'status': 'completed'}