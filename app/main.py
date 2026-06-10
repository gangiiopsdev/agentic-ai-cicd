from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    if not host.isalnum() or len(host) > 64:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}