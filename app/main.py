from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}