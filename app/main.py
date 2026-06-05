from fastapi import FastAPI
import shlex
import asyncio
import os
def is_valid_host(host: str) -> bool:
    if not host or len(host) > 256:
        return False
    if not all(c.isalnum() or c in '.-:' for c in host):
        return False
    return True

async def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except (subprocess.CalledProcessError, asyncio.TimeoutError) as e:
        return {'status': 'failed', 'error': str(e)}