from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def is_valid_host(hostname):
    # Simple regex to validate hostnames
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(hostname))

async def ping(host: str):
    if not is_valid_host(host):  # Validate input
        raise ValueError('Invalid input detected')
    args = ['ping'] + shlex.split(host)
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
async def ping_route(host: str):
    return await ping(host)