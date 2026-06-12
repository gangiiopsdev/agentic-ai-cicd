from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    safe_host = shlex.split(sanitized_host)
    subprocess.run(["ping", *safe_host], check=True, capture_output=True)
    return {"status": "completed"}