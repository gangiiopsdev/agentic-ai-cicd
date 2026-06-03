from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid input')
        args = shlex.split(f'ping -c 1 {host}')  # Limiting the number of pings for security
        subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}