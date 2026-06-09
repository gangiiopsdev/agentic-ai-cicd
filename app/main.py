from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Enhanced implementation using subprocess.run with shell=False and validate the host input
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Enhanced validation logic for host
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))