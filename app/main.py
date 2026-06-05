from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
from subprocess import Popen, PIPE

app = FastAPI()

def is_safe_host(host):
    # Enhanced validation example: allow only alphanumeric characters and a few common separators
    return host.isalnum() or '.' in host or '-' in host

def sanitize_host(host):
    safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join([char for char in host if char in safe_chars])
    return sanitized_host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not is_safe_host(sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        process = Popen(['ping', '-c 1', f'"{sanitized_host}"'], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            raise Exception(error.decode())
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}