from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isdigit() or len(host) > 32 or '/' in host or '.' not in host:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}