from fastapi import FastAPI
import asyncio
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add your list of allowed hosts here
    if host in allowed_hosts:
        args = [shlex.quote(arg) for arg in shlex.split(f'ping {host}')]  # Escape arguments
        process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    else:
        return {'status': 'denied'}