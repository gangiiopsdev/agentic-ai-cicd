from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Basic host validation and escaping
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' 
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}")

    return {"status": "completed"}