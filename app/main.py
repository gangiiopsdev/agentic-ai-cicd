from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ["ping", "-c", "4", host]
    try:
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': stderr}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)