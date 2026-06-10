from fastapi import FastAPI
import subprocess
import shlex
global allowed_hosts
allowed_hosts = ['127.0.0.1', 'localhost']
app = FastAPI()
def validate_host(host):
    return host in allowed_hosts
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host specified')
    # Use shlex.quote to safely escape the user input
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.stderr}
    return {'status': 'completed', 'output': result.stdout}