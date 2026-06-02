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
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}