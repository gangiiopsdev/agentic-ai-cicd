from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
import os

app = FastAPI()

async def ping_host(host):
    if not validate_host(host):
        raise ValueError('Invalid host name')

    # Use subprocess.run with shell=False to avoid command injection
    cmd = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}

async def validate_host(host):
    # Simple validation example: allow only alphanumeric characters and dots
    import re
    return bool(re.match(r'^[a-zA-Z0-9.]+$', host))