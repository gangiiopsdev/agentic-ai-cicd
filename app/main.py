from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if not re.match('^[a-zA-Z0-9]*$', host):  # Use regex to ensure only alphanumeric characters are allowed
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}