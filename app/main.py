from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shell escaping and validation
    safe_host = quote(host)
    if not is_safe_host(safe_host):
        raise ValueError("Invalid host input")
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}

def is_safe_host(host: str) -> bool:
    # Basic validation to ensure the host does not contain unexpected characters
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    return all(char in allowed_chars for char in host)