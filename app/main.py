from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return {"status": "completed"}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation to prevent command injection
    if not host.isalnum() or '.' in host:
        return {'error': 'Invalid host'}
    return await ping(host)