from fastapi import FastAPI
import os
import shlex
import asyncio
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain unexpected characters
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        safe_host = shlex.quote(host)
        args = ['ping', '-c', '4', safe_host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}