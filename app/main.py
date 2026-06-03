from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def safe_command(command: str) -> list:
    return shlex.split(command)

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
async def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(safe_command(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}