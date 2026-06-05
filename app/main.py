from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    try:
        command = ['ping'] + shlex.split(host)
        subprocess.run(command, check=True, timeout=5)
        return True
    except Exception as e:
        print(e)
        return False

def safe_host(host):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        safe_host(host)
        return {'status': 'completed', 'result': 'success'}
    except ValueError as e:
        return {'status': 'failed', 'result': str(e)}