from fastapi import FastAPI
import subprocess
import re

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_ip_address(ip_address):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return pattern.match(ip_address)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_ip_address(sanitize_host(host)) is None:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', f'-c 1 {shlex.quote(sanitize_host(host))}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}