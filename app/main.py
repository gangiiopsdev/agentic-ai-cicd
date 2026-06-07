from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'  # Adjust as needed
    return ''.join(c for c in host if c in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}