from fastapi import FastAPI
import subprocess
import shlex
import os
def safe_ping(host: str):
    args = ['ping', '-c', '4', host]
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if os.path.basename(host) == host and not any(c in host for c in [';', '|', '&', '`', '$']):  # Enhanced check to prevent shell injection
        return safe_ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid input'}