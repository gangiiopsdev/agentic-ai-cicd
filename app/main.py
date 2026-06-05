from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host or '.' not in sanitized_host:
        return {'status': 'error', 'message': 'Invalid host input'}
    result = subprocess.run(shlex.split('ping ' + sanitized_host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}