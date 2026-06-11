from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if len(sanitized_host) > 255:
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}