from fastapi import FastAPI
import os
import shlex
import subprocess

class Sanitizer:
    def __init__(self):
        self.allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')

    def sanitize(self, host: str) -> str:
        return ''.join(c for c in host if c in self.allowed_chars)

app = FastAPI()
sanitizer = Sanitizer()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitizer.sanitize(host)
    if not sanitized_host:
        return {'error': 'Invalid host name'}
    try:
        result = subprocess.run(['/usr/bin/ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr)}
    return {'status': 'completed'}