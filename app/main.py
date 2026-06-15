from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
        return {
            'status': 'completed',
            'stdout': result.stdout.decode(),
            'stderr': result.stderr.decode()
        }
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}