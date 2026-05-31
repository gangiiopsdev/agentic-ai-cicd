from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

def execute_ping(host: str):
    try:
        subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr)}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'error': 'Invalid host name'}
    result = execute_ping(sanitized_host)
    return result