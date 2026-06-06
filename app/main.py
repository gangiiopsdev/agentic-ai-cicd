from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate and sanitize the host input
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)