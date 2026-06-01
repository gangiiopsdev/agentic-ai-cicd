from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def escape_shell_arg(s):
    if not isinstance(s, str):
        raise ValueError('Argument must be a string')
    return shlex.quote(s)

async def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    safe_host = escape_shell_arg(host)
    args = ['ping', safe_host]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}