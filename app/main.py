from fastapi import FastAPI
import subprocess
import os
import shlex

def validate_host(host):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return True

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}