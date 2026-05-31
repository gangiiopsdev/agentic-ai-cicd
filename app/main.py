from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'error': 'Invalid host name'}
    try:
        subprocess.run(['ping', '-c', '1', shlex.quote(sanitized_host)], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr)}
    return {'status': 'completed'}