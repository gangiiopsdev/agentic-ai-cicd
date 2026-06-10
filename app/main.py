from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in host if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse({'status': 'completed', 'output': output.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse({'status': 'failed', 'error': e.output.decode()}, status_code=400)