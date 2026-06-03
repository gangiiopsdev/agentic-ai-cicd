from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with proper validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}