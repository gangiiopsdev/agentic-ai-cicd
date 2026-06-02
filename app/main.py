from fastapi import FastAPI
import subprocess
from shlex import quote
import asyncio

app = FastAPI()

def safe_ping(host: str):
    quoted_host = quote(host)
    return 'ping', quoted_host

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec(*safe_ping(host), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():  # Simplified validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)