from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

def validate_command(command):
    pattern = r'^ping [a-zA-Z0-9.-_]+$'
    return re.match(pattern, command) is not None

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    if validate_command(f'ping {safe_host}'):
        args = shlex.split(f'ping {safe_host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        return {"status": "invalid command"}