from fastapi import FastAPI
import subprocess
import shlex
global host_whitelist = { 'google.com', 'example.com' }

app = FastAPI()

async def ping(host: str):
    if host in host_whitelist:
        # Secure implementation
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)