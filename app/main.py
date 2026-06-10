from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_hostname(hostname):
    return hostname.strip().replace(' ', '').replace('\t', '')

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_hostname(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'error': 'Invalid hostname'}, 400
    args = shlex.split(f'ping -c 1 {sanitized_host}')
    result = subprocess.run(['ping', *args], capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}, result.returncode
    return {'status': 'completed', 'output': result.stdout}