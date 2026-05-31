from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it is safe
        if not host.isalnum() or len(host) > 255:
            return {'status': 'failed', 'error': 'Invalid host'}
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            return {'status': 'failed', 'error': result.stderr}
        return {'status': 'completed'}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': 'Command timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}