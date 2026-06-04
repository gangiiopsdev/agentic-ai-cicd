from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_string if c in safe_chars)

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f'ping {quote(sanitized_host)}')
    return {'status': 'completed'}