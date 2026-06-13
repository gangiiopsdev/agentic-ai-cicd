from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    # Secure implementation
    command = ['/bin/ping', host]
    result = await asyncio.create_subprocess_exec(*command, check=True)
    return {'status': 'completed'}