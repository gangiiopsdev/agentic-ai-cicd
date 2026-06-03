from fastapi import FastAPI
import asyncio
from urllib.parse import urlparse

app = FastAPI()

allowed_hosts = {'google.com', 'example.com'}

async def ping(host: str):
    parsed_host = urlparse(host)
    host_without_protocol = parsed_host.netloc
    if not allowed_hosts.intersection({host_without_protocol}):
        raise ValueError('Invalid host')
    # Use a whitelist of allowed parameters and avoid passing user input directly to subprocess.run()
    result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', host_without_protocol], capture_output=True, text=True, check=True)
    return result.stdout

async def ping_route(host: str):
    try:
        output = await ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}