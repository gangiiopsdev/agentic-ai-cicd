from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(c for c in host if c in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", sanitize_host(host)])
    return {"status": "completed"}