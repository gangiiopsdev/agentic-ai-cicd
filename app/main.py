from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def safe_ping(host):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    # Use a whitelist approach to allow only numeric hosts
    if all(char.isdigit() for char in host):
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)