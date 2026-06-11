from fastapi import FastAPI
import subprocess
import re
import shlex

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to avoid flooding
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}