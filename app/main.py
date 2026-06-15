from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host input to prevent shell injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        args = shlex.split(f'ping {host}')
        subprocess.call(args, shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500