from fastapi import FastAPI
import asyncio
import shlex
import subprocess

async def safe_ping(host: str):
    try:
        command = ['ping', '-c', '1', host]
        output = await asyncio.to_thread(subprocess.check_output, command, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)