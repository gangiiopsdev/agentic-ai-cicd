from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status

app = FastAPI()

async def validate_host(host: str) -> None:
    if not host.isalnum():
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '--', quote(host)]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}