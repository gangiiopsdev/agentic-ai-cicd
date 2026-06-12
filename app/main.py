from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    sanitized_host = shlex.quote(host)
    result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}