from fastapi import FastAPI
import subprocess
import shlex
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    allowed_hosts = ['example.com', 'test.com']  # Example whitelist
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        result = subprocess.run(['ping', '-c', '4', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except cimport as e:
        return {'status': 'failed', 'error': e.stderr}