from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):    sanitized_host = sanitize_host(host)    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid input'}    args = ['ping', quote(sanitized_host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}