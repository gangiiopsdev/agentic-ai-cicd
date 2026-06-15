from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def secure_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    if result.returncode != 0:
        raise Exception(f'Ping failed: {stderr.decode()}')

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed'}