from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def is_valid_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

async def ping(host: str):
    if not await is_valid_host(host):
        raise ValueError('Invalid host name')
    result = await subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    try:
        result = await ping(host)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}