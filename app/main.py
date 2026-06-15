from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

def validate_host(host):
    pattern = r'^[a-zA-Z0-9-.]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    sanitized_host = sanitize_host(host)
    try:
        command = shlex.split(f'ping -c 1 {sanitized_host}')
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}