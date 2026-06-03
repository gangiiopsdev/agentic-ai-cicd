from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        return False
    valid_hosts = ['example.com', 'test.com']
    return host in valid_hosts