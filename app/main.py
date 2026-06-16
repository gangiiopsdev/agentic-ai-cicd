from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

def is_valid_host(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return host in ['127.0.0.1', 'localhost']
    except ValueError:
        return False

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return await ping(host)