from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    if not host.isalnum() or not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        return {'status': 'error', 'output': 'Invalid input'}
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '-.')
    subprocess.run(['ping', quote(sanitized_host)])

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        sanitized_host = ''.join(c for c in host if c.isalnum() or c in '-.')
        result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}