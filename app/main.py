from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    # More comprehensive regex to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9._%+-]', '', host)
    return sanitized_host

async def secure_ping(host: str):
    if not sanitized_host:
        raise ValueError('Invalid host name')
    args = ['ping', sanitized_host]
    await asyncio.create_subprocess_exec(*args, shell=False)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    secure_ping(sanitized_host)
    return {'status': 'completed'}