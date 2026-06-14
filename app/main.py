from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    try:
        await asyncio.create_subprocess_exec(*args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
async def ping(host: str):
    result = await safe_ping(host)
    if 'error' in result:
        return result
    return {'status': 'completed'}