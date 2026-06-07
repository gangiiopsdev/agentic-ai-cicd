from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Regular expression to validate host format
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failure', 'error': 'Invalid host'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failure', 'error': 'Invalid host'}
    return ping(host)