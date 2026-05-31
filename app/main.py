from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import os

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    host = credentials.credentials
    if not host.startswith('192.168.') or ':' in host:
        return {'status': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}