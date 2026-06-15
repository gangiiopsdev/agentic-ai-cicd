from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

import re
def validate_host(host: str) -> bool:
    pattern = re.compile(r"^[a-zA-Z0-9.-]+$")
    return bool(pattern.match(host))