from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}

    try:
        output = subprocess.check_output(['ping', f'-c 1 {host}'], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping_endpoint(host: str):
    result = ping(host)
    return result