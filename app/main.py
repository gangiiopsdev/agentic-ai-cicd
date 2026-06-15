from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host or len(host) > 256:
        raise ValueError("Invalid host parameter")
    # Use a whitelist of allowed hosts
    allowed_hosts = ["example.com", "test.com"]
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}