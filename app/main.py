from fastapi import FastAPI
import subprocess
import os
def sanitize_host(host):
    allowed_hosts = {"example.com", "test.example.com"}
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', os.path.abspath(sanitized_host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}