from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(c for c in host if c in allowed_chars)
    return sanitized
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', sanitize_host(host)]
    subprocess.call(command)
    return {"status": "completed"}