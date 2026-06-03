from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts
@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output.decode())}