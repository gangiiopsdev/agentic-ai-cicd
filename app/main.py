from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

def ping(host: str):
    sanitized_host = sanitize_host(host)
    if len(sanitized_host) > 255:
        raise ValueError("Invalid hostname")
    subprocess.call(shlex.split(f'ping {sanitized_host}'))

app = FastAPI()

@app.get("/ping")
def ping_api(host: str):
    return ping(host)