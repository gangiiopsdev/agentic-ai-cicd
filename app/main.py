from fastapi import FastAPI
import subprocess
import shlex
import asyncio

async def ping(host: str):
    try:
        args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
        result = await asyncio.subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}