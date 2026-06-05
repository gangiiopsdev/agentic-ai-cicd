from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = shlex.split(f'ping {host}')  # Remove shlex.quote to avoid unnecessary quoting
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}