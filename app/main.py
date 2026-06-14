from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['192.168.0.1', '172.16.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}