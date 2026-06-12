from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import shlex

app = FastAPI()
security = HTTPBasic()

def safe_ping(host):
    # Ensure host is a valid IP address or hostname to prevent command injection
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

def validate_host(host):
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials):
    host = credentials.username
    safe_ping(host)
    return {"status": "completed"}