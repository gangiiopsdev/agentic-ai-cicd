from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host name')
    command = ['ping'] + shlex.split(host)
    result = await asyncio.create_subprocess_exec(*command, capture_output=True, text=True)
    return {'stdout': result.stdout.strip(), 'stderr': result.stderr.strip()}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)