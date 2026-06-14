from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}