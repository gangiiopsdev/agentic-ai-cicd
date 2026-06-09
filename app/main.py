from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}