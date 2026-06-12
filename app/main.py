from fastapi import FastAPI
import subprocess
from typing import Optional
from shlex import quote
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

async def authenticate_token(token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Add token validation logic here
    return True

def sanitize_input(input_str):
    return subprocess.list2cmdline([input_str])

@app.get("/ping")
def ping(host: Optional[str] = None, token: HTTPAuthorizationCredentials = Depends(authenticate_token)):
    if host is None or not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(sanitized_host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}