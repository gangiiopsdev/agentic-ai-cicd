from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            raise ValueError(f'Invalid character in host: {char}')
app = FastAPI()
def ping(host: str):
    validate_host(host)
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, check=True, text=True, shell=False)
    if result.returncode == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': result.stderr}
@app.get('/ping')
def ping_safe(host: str):
    validate_host(host)
    # Sanitize the input to prevent injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '-.')
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, text=True, shell=False)
    if result.returncode == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': result.stderr}