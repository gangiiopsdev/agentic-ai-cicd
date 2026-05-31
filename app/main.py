from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError('Invalid input')
    return input_str

async def secure_ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    await asyncio.create_subprocess_exec(*args)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}