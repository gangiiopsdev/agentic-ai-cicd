from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import os

app = FastAPI()
bearer_scheme = HTTPBearer()

def safe_ping(host):
    if not host.startswith('192.168.') or ':' in host:
        return {'status': 'Invalid host'}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': str(e)}

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return safe_ping(credentials.credentials)