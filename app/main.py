from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status

app = FastAPI()

def validate_host(host: str) -> None:
    if not host.isalnum():
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '--', quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result.stderr)
    return {'status': 'completed'}