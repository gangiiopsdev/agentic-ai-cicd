from fastapi import FastAPI
import subprocess
import shlex
def validate_input(host):
    if not host.replace('.', '').isdigit() and ':' not in host:
        raise ValueError('Invalid host format')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, shell=False)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}