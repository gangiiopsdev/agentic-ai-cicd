from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with proper validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)