from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent command injection
    if not host.isalnum() or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}