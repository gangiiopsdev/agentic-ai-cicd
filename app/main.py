from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import secrets
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized = ''.join(filter(lambda x: x in allowed_chars, input_str))
    return sanitized
app = FastAPI()
bearer_scheme = HTTPBearer()
@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 256:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', '--', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}