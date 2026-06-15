from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def validate_host(host):
    if not host.isalnum():
        return False
    # Additional validation can be added here, e.g., checking against a whitelist
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host name'}

    try:
        subprocess.run(['ping', '-c 1', f'"{host}"'], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error code {e.returncode}'}
    return {'status': 'completed'}