from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = ['ping'] + shlex.split(shlex.quote(host))  # Use shlex.quote for proper quoting
    subprocess.run(args, check=True)
    return {'status': 'completed'}