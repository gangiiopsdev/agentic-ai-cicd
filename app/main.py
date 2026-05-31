from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

async def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    await asyncio.create_subprocess_exec(*args)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}