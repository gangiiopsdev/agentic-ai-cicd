from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host')
    ping_command = ['ping', quote(host)]
    result = subprocess.run(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return result.stdout.decode()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}