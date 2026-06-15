from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', shlex.quote(host)]  # Use shlex.quote for safe argument passing
    subprocess.call(args)
    return {'status': 'completed'}