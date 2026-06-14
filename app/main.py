from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', *shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

import re

def is_safe_host(host: str) -> bool:
    # Define a regular expression pattern for safe hosts
    pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, host) is not None