from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    return re.sub(r'[^a-zA-Z0-9.-]', '', host)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Validate host input
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}