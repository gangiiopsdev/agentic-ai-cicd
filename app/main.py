from fastapi import FastAPI
import shlex
from fastapi import HTTPException
import asyncio
import subprocess

app = FastAPI()

def is_valid_host(host: str):
    # Add validation logic for the host name here
    return True

def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host name")
    args = ['ping', '-c', '1', shlex.quote(host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}