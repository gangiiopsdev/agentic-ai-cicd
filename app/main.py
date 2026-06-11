from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        output = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    validate_host(host)
    return ping(host)