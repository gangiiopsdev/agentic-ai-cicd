from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific IP addresses or domain names
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

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