from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

def safe_ping(host: str) -> Dict[str, str]:
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)