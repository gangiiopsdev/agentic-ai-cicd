from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os

app = FastAPI()
security = HTTPBasic()

def verify_password(username: str, password: str):
    return username == 'admin' and password == 'secret'

def safe_ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    return result.stdout

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if not verify_password(username, password):
        return {'status': 'failed', 'error': 'Invalid credentials'}
    host = credentials.username  # Assuming username is the host to ping
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}