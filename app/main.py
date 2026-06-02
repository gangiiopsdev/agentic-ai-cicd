from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper validation
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}