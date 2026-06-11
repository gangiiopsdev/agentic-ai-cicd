from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' + '.'.join(subprocess.getoutput('ping -c 1 google.com').splitlines()[1].split())
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not all(c.isalnum() or c in ('.', '-', '_') for c in sanitized_host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}