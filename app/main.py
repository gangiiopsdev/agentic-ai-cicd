from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):  # Regex to allow alphanumeric characters and punctuation
        return {'error': 'Invalid host'}, 400

    args = shlex.split(f'ping {host}')
    subprocess.run(['ping'] + args, check=True)

    return {'status': 'completed'}