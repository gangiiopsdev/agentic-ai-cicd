from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_str if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    host = sanitize_input(host)
    if not host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping'] + shlex.split('-c 1 "' + re.escape(host) + '"'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}