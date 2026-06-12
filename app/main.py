from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host: str):
    if not host.strip():
        return None
    # Allow only a-z, A-Z, 0-9, and common domain characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {'status': 'error', 'message': 'Invalid input'}
    # Regex to validate the host format
    host_regex = re.compile(r'^[a-zA-Z0-9.-_]+$')
    if not host_regex.match(sanitized_host):
        return {'status': 'error', 'message': 'Invalid host format'}
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}