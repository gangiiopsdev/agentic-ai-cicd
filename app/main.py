from fastapi import FastAPI
import os
import shlex
import asyncio
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        args = ['ping', safe_host]
        process = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, ' '.join(args), output=stderr)
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}