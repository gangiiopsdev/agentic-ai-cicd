from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = await sanitize_host(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}