from fastapi import FastAPI
import subprocess
import shlex
import re
def safe_ping(host):
    # Ensure host is a valid IP address or hostname
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and ('.' in host or ':' in host):
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid host'}
    try:
        result = subprocess.check_output(shlex.split(f'ping -c 1 {shlex.quote(host)}'), stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}
    return {'status': 'completed'}