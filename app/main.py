from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}