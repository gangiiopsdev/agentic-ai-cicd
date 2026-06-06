from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Simple validation to prevent common attacks
    if not host.replace('.', '').isdigit():
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.check_output(['ping'] + shlex.split(host), stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'result': result.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}