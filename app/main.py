from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum() and not all(c in '-.' for c in host):
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}