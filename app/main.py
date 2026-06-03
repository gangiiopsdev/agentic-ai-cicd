from fastapi import FastAPI
import subprocess
import shlex
import re

global_count = 0

app = FastAPI()

def safe_ping(host):
    global global_count
    # Safe implementation using shlex.quote to escape arguments and logging
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    print(f'Ping executed {global_count} times: {result.stdout}')
    global_count += 1

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}

def validate_host(host):
    # Simple validation to ensure the host is a valid IP or hostname
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None