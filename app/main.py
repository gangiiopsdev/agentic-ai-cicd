from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

def execute_safe_ping(host):
    # Validate the sanitized host more strictly to ensure it's a valid hostname
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid host")
    command = ['ping', host]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    execute_safe_ping(sanitized_host)

    return {"status": "completed"}