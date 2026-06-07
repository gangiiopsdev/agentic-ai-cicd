from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use a whitelist for allowed hosts instead of regex validation.
    allowed_hosts = ['host1', 'host2']  # Example list, replace with actual allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', '-c', str(4), shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}