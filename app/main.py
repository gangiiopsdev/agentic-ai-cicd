from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def is_valid_ip(ip_address):
    parts = ip_address.split('.')
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if is_valid_ip(sanitized_host):
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.run(args, check=True, shell=False)
        return JSONResponse(content={"status": "completed"}, status_code=200)
    else:
        return JSONResponse(content={"error": "Invalid IP address"}, status_code=400)