from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper quoting
    subprocess.run(['ping', quote(host)], check=True)

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise ValueError("Invalid host")
    safe_ping(host)
    return {"status": "completed"}

def valid_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts