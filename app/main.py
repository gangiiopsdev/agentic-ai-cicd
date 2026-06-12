from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host name'}

    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error code {e.returncode}'}
    return {'status': 'completed'}