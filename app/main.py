from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['google.com', 'example.com']
    return host in allowed_hosts

async def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
    return result.stdout

def ping_route(host: str):
    try:
        output = ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}