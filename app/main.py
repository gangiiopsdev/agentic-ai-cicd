from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    try:
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        await asyncio.create_subprocess_exec(*args)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)