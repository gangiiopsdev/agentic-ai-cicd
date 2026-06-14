from fastapi import FastAPI
import subprocess
import shlex
import re

def validate_host(host: str) -> bool:
    # Regex to allow only IP addresses and domains
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}