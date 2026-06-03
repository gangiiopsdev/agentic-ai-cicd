from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def execute_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        error = await result.stderr.read()
        return {'status': 'failed', 'error': error.decode()}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not is_valid_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return await execute_ping(host)

import re

def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None