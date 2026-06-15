from fastapi import FastAPI
import asyncio
import re
from shlex import quote

app = FastAPI()

def safe_ping(host):
    try:
        # Validate host using a regular expression for simplicity
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        output = await asyncio.create_subprocess_exec('ping', quote(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            return {'status': 'failed', 'error': stderr.decode()}
        return {'status': 'completed', 'output': stdout.decode()}
    except asyncio.TimeoutError as e:
        return {'status': 'failed', 'error': 'Command timed out'}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    return await safe_ping(host)

async def is_safe_host(host):
    # Implement logic to validate the host
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts