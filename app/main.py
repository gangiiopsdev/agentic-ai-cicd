from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return re.match(pattern, host) is not None

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid hostname")
    sanitized_host = sanitize_input(host)
    try:
        args = shlex.split(f'ping -c 4 {sanitized_host}')
        subprocess.run(args, check=True, shell=False)
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}