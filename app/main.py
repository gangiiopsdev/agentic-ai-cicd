from fastapi import FastAPI
import subprocess
import shlex
import asyncio
global args
args = ['ping', '127.0.0.1']

app = FastAPI()

async def secure_ping(host: str):
    # Sanitize the host input using a whitelist approach
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host name')
    args[1] = host
    await asyncio.create_subprocess_exec(*args)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}