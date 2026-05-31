from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host specified')
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

    return {'status': 'completed'}