from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}