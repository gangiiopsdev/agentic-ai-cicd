from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def ping(host: str):
    if not host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid input'}
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True)

    return {'status': 'completed'}