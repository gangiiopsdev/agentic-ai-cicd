from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {shlex.quote(host)}')
    await subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)