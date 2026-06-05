from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_host(host: str):
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in safe_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid input'}

    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)  # Set check=False to avoid exception on non-zero exit codes

    return {'status': 'completed', 'output': result.stdout}