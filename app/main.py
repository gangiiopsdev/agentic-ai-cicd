from fastapi import FastAPI
import subprocess
import shlex
from sanic.response import json

async def ping(host: str):
    if not host.isdigit() or host.startswith('-'):
        raise ValueError('Invalid input')
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return json({'status': 'completed', 'output': output.decode().strip()})
    except Exception as e:
        return json({'status': 'error', 'message': str(e)})

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isdigit() or host.startswith('-'):
        raise ValueError('Invalid input')
    return await ping(host)