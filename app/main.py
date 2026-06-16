from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host: str) -> bool:
    # Add validation logic for the host
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    safe_command = shlex.split(f'ping {host}')
    subprocess.call(safe_command)
    return {"status": "completed"}