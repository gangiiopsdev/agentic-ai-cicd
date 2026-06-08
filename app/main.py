from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            raise ValueError(f'Invalid character in host: {char}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    escaped_host = escape_host(host)
    try:
        result = subprocess.run(['ping', '-c 1', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}