from fastapi import FastAPI
import subprocess
import shlex
import re
import asyncio

app = FastAPI()

def safe_ping(host: str):
    if host not in ('127.0.0.1', 'localhost'):
        return {'error': 'Unauthorized ping attempt'}
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host name'}
    try:
        command = ['ping', '-c', '4'] + shlex.split(host)
        output = await asyncio.to_thread(subprocess.check_output, command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)