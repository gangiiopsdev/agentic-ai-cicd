from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, host))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_host(host))
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}