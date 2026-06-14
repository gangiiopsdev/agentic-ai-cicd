from fastapi import FastAPI
import shlex
import asyncio
import subprocess
import re

app = FastAPI()

async def ping_safe(host: str):
    # Use a more comprehensive regex for validating hostnames
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    try:
        safe_host = shlex.quote(host)
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=error)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)