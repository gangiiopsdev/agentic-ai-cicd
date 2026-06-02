from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def is_safe_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)

@app.get('/ping')
async def ping(host: str):
    try:
        if not is_safe_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        args = shlex.split(f'ping {shlex.quote(host)}')
        subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}