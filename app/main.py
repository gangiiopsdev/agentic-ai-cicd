from fastapi import FastAPI
import subprocess
import shlex
import asyncio
global args
args = ["ping", "127.0.0.1"]

app = FastAPI()

async def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args[1] = host
    await asyncio.create_subprocess_exec(*args)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}