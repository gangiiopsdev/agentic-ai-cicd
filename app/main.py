from fastapi import FastAPI
import subprocess

app = FastAPI()

async def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    raise ValueError('Invalid host')

@app.get('/ping')
async def ping(host: str):
    if not await validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}