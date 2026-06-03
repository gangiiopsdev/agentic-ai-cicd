from fastapi import FastAPI
import subprocess
import shlex
from typing import List, Union

app = FastAPI()

async def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in '.-' for c in host)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid input detected in host parameter')
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}