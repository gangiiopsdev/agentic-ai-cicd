from fastapi import FastAPI
import subprocess
from shlex import quote
import asyncio

app = FastAPI()

async def ping(host: str):
    try:
        safe_host = await asyncio.to_thread(quote, host)
        result = await asyncio.create_subprocess_exec('ping', safe_host, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():  # Simplified validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)