from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '..' in host:
        return {'status': 'error', 'output': 'Invalid input'}
    # Secure implementation using subprocess.run with shell=False and executable specified
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}