from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    try:
        return all(c.isdigit() or c in '0123456789.' for c in host)
    except TypeError:
        return False
def is_allowed_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list, customize as needed
    return host in allowed_hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host) or not is_allowed_host(host):
        return {'status': 'failed', 'error': 'Invalid or unauthorized host'}
    args = shlex.split(f'ping -c 1 {host}')  # Limiting the number of pings for security
    try:
        subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}