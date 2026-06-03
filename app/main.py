from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return all(c.isalnum() or c in '.:-_' for c in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400

    args = shlex.split(f'ping {host}')
    subprocess.run(['ping', host], check=True)

    return {'status': 'completed'}