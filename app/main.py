from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Basic validation and sanitization of host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(["ping", escaped_host], check=True)
    return {"status": "completed"}