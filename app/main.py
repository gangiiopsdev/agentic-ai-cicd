from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    # Simple sanitization example
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping -c 1 {sanitized_host}')
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)