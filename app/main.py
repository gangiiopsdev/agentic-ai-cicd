from fastapi import FastAPI
import asyncio
import shlex
import subprocess as sp

app = FastAPI()

async def ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    command = f'ping {shlex.quote(sanitized_host)}'
    result = await asyncio.create_subprocess_exec('ping', sanitized_host, stderr=sp.PIPE)
    output, _ = await result.communicate()
    return {'status': 'completed', 'result': output.decode('utf-8')}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)