from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        raise ValueError('Invalid host format')
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}

import re
def is_valid_host(host):
    # Simple regex to validate host format (IP address or domain name)
    pattern = r'^[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, host))