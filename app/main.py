from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Simple validation for demonstration purposes
    return '.' in host and len(host.split('.')) == 4