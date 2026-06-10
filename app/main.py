from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    return ''.join(filter(str.isalnum, host))
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    try:
        subprocess.run(args, check=True, shell=False, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}