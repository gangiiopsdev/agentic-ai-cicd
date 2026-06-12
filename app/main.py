from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host):
    # Validate host to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, args, output=output, stderr=error)

@app.get('/ping')
def ping(host: str):
    try:
        await safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}