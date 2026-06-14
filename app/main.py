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

    # Use subprocess.run with shell=False and validate arguments explicitly
    args = ['ping', '-c', '4', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_api(host: str):
    return ping(host)