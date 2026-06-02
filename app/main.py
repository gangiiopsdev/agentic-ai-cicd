from fastapi import FastAPI
import asyncio
import shlex
import re

app = FastAPI()

async def secure_ping(host: str):
    # Use shlex.quote to properly escape arguments
    args = ['ping', shlex.quote(host)]
    await asyncio.create_subprocess_exec(*args)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}