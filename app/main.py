from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}