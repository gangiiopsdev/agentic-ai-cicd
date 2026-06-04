from fastapi import FastAPI
import shlex
import asyncio
import os

async def ping(host: str):
    # Validate the input to prevent command injection
    if not host or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    if not all(c.isalnum() or c in '.-:' for c in host):
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}

    try:
        args = shlex.split('ping ' + host)
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except (subprocess.CalledProcessError, asyncio.TimeoutError) as e:
        return {'status': 'failed', 'error': str(e)}