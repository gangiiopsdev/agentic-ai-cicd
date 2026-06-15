from fastapi import FastAPI
import asyncio
import subprocess
from sanic.response import json

app = FastAPI()

def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in ['.', '-'] for c in host)

async def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return json({'status': 'completed' if result.returncode == 0 else 'error', 'output': output.decode()})
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.stderr.decode())}