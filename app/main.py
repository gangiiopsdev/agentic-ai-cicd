from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        args = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}