from fastapi import FastAPI
import subprocess
import asyncio
from urllib.parse import urlparse

app = FastAPI()

allowed_hosts = {'google.com', 'example.com'}

async def ping(host: str):
    parsed_host = urlparse(host)
    host_without_protocol = parsed_host.netloc
    if not allowed_hosts.intersection({host_without_protocol}):
        raise ValueError('Invalid host')
    result = await asyncio.to_thread(subprocess.run, ['ping', host_without_protocol], capture_output=True, text=True, check=True)
    return result.stdout

def ping_route(host: str):
    try:
        output = ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}