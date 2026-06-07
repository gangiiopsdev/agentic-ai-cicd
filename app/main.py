from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Enhanced validation to prevent command injection
    if not host.replace('.', '').isdigit():
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, timeout=10)
        return {'status': 'completed', 'result': result.stdout}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'error': e.stderr}