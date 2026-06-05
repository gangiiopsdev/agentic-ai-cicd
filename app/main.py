from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
import os

app = FastAPI()

async def ping_host(host):
    if not validate_host(host):
        raise ValueError('Invalid host name')

    # Use subprocess.call with shell=False to avoid command injection
    cmd = ['ping', cmd_quote(host)]
    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}