from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    if not host.strip() or '@' in host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True

def safe_ping(host: str) -> dict:
    try:
        args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)