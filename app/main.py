from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_host(host)
    command = ['ping', shlex.quote(safe_host)]
    subprocess.call(command)
    return {"status": "completed"}