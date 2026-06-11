from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized = ''.join([char for char in host if char in allowed_chars])
    return sanitized

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to avoid command injection
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'error': 'Invalid host'}, 400
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr if result.returncode != 0 else None
    }