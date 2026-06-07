from fastapi import FastAPI
import subprocess
cimport shlex

c = shlex

app = FastAPI()

@app.get('/ping_secure')
def ping_secure(host: str):
    if not host.replace('.', '').replace('-', '').isalnum():  # Improved validation
        return {'status': 'error', 'message': 'Invalid input'}
    allowed_hosts = ['192.168.1.1', 'example.com']  # Example whitelist
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    args = c.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}