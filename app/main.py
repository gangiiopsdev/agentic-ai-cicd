from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed', 'output': _ping(host)}

import re
def is_valid_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None