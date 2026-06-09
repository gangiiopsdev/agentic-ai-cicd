from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(input_host):
    allowed_hosts = ['example.com', 'localhost']  # List of safe hosts
    return input_host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        args = ['ping', '-c', '1'] + shlex.split(shlex.quote(host))  # Use shlex.quote to escape user input
        subprocess.run(args, check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}