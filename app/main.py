from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def secure_ping(host):
    args = ['ping', host]
    await asyncio.create_subprocess_exec(*args, check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or len(host) != 3:
        raise ValueError('Invalid host input')
    await secure_ping(host)
    return {'status': 'completed'}