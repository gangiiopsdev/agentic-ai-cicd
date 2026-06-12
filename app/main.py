from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    if not host.strip() or len(host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return output.decode().strip()

@app.get('/ping')
def ping(host: str):
    return {'result': safe_ping(host)}