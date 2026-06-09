from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError('Invalid host input')

    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

    return {'status': 'completed'}