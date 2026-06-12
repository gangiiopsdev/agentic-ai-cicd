from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

def sanitize_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in host if char in allowed_chars)

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise HTTPException(status_code=400, detail='Invalid host name')
    result = subprocess.run(['ping', '--'], [sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}