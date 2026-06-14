from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping_command(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return shlex.split(f'ping {host}')

@app.get('/ping')
def ping(host: str):
    args = ['ping', *safe_ping_command(host)]
    subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}