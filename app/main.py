from fastapi import FastAPI
import subprocess

async def safe_ping(host: str) -> dict:
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts