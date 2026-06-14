from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ["ping", sanitized_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}