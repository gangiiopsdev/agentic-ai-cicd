from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(hostname):
    # Implement a whitelist of allowed hosts or use a more secure method to validate input
    return hostname in ['allowed_host1', 'allowed_host2']
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host provided')
    # Safe implementation with shell=False and proper input sanitization
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}