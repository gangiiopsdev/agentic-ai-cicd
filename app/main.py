from fastapi import FastAPI
import subprocess
from typing import List

allowed_hosts: List[str] = ['example.com', 'test.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c 1', '--', host], check=True, timeout=5, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except subprocess.TimeoutExpired as e:
        return {'status': 'error', 'message': 'Command timed out'}