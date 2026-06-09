from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

def is_safe_host(host: str):
    # Implement logic to check if the host is safe to ping
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts