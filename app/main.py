from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Ensure the host input is safe to use with subprocess
        if not os.path.exists(host) or '/' in host:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}