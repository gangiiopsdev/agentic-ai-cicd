from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
import os

app = FastAPI()
security = HTTPBasic()
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username
    # Sanitize input to avoid command injection
    if not all(char.isalnum() or char in ['-', '.', '_', ':', '/'] for char in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        subprocess.run(['ping', f'/bin/ping {host}'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}