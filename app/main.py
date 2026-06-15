from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255:
        return False
    # Validate the host using a whitelist approach
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'output': str(e)}