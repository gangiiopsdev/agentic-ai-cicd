from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}