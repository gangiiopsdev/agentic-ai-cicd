from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    # Define a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host is not in the allowed list')

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True, shell=False)  # Ensure shell=False to prevent command injection
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}