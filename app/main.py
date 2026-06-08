from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid characters in host")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    sanitized_host = shlex.quote(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}