from fastapi import FastAPI
import subprocess
from shlex import quote
import asyncio

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = await asyncio.create_subprocess_exec('ping', quote(host), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():  # Simplified validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)