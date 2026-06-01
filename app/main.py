from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def ping(host: str):
    # Validate input
    if not host or ' ' in host:
        raise ValueError('Invalid hostname')
    result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get('/ping/')
def ping_route(host: str):
    try:
        output = await ping(host)
        return {'status': 'completed', 'output': output}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'output': str(e)}