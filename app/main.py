from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException
import os

def ping_host(host):
    if not host:
        raise HTTPException(status_code=400, detail='Host parameter is required')
    cmd = ['ping', shlex.quote(host)]  # Use shlex.quote to escape user input
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}