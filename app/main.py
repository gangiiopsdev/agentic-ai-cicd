from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

async def ping(host: str):
    # Ensure the host parameter is sanitized to avoid command injection
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)