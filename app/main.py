from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        raise Exception(error.decode('utf-8'))

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    try:
        return await ping(host)
    except Exception as e:
        return {'error': str(e)}

import re

async def validate_host(host: str) -> bool:
    # Basic validation, can be expanded for more robustness
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))