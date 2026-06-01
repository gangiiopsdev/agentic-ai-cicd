from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return await safe_ping(host)

import re

def validate_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None