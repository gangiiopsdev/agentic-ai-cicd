from fastapi import FastAPI
import subprocess
from typing import List

allowed_hosts = ['example.com', 'another-example.com']

async def run_ping(host: str) -> str:
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        output = await asyncio.subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
async def ping(host: str):
    return await run_ping(host)