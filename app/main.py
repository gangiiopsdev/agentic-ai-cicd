from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def run_safe_ping(host: str):
    # Define allowed hosts or use whitelist/blacklist approach
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}

    args = shlex.split(f'ping {host}')
    try:
        result = await app.state.asyncio_pool.run(subprocess.run, args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    return run_safe_ping(host)