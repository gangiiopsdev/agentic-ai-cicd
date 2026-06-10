from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization example
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Secure implementation
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}