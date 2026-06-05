from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def is_valid_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def ping_safe(host: str):
    if not await is_valid_host(host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):