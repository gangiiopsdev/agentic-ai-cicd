from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host) or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}