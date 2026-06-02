from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

async def secure_ping(host: str):
    # Sanitize the host input using a regular expression
    sanitized_host = re.sub(r'[^a-zA-Z0-9]', '', host)
    if not sanitized_host:
        raise ValueError('Invalid host name')
    args = ['ping', sanitized_host]
    await asyncio.create_subprocess_exec(*args, shell=False)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}