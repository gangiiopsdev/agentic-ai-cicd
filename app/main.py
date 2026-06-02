from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    # Simple sanitization example
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(["ping", sanitized_host], shell=False)  # Ensure shell=False to prevent command injection
    return {"status": "completed"}