from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Basic validation, can be expanded
    return 'example.com' in host