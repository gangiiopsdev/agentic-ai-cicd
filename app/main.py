from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import os
def validate_host(host):
    return host.startswith('192.168.') and ':' not in host

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    host = credentials.credentials
    if not validate_host(host):
        return {'status': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}