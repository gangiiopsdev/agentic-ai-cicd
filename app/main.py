from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'stderr': 'Invalid host name'}

    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', *shlex.split(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)