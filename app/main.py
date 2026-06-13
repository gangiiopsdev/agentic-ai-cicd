from fastapi import FastAPI
import subprocess
import shlex
from typing import Union

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.strip().isalnum() and '..' not in host

def sanitize_command(command_parts: list) -> list:
    sanitized_parts = []
    for part in command_parts:
        if isinstance(part, str):
            sanitized_part = shlex.quote(part)
            sanitized_parts.append(sanitized_part)
        else:
            sanitized_parts.append(part)
    return sanitized_parts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        command_parts = ['ping'] + shlex.split(host)
        sanitized_command = sanitize_command(command_parts)
        result = subprocess.run(sanitized_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}