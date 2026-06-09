from fastapi import FastAPI
import subprocess
from typing import List
def safe_ping(host: str) -> bool:
    return host in ['example.com', 'test.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c 1', host], check=True, timeout=5, capture_output=True, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except subprocess.TimeoutExpired as e:
        return {'status': 'error', 'message': 'Command timed out'}