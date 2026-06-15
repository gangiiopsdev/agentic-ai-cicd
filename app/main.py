from fastapi import FastAPI
import re
import subprocess

async def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result.stdout.decode('utf-8')

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
ping