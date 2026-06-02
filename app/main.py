from fastapi import FastAPI
import asyncio
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    # Validate host input to ensure it's a valid IP or hostname
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host) and not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'error': 'Invalid host'}
    return ping(host)