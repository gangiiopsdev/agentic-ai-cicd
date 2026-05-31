from fastapi import FastAPI, HTTPException
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}

def is_safe_host(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return host in allowed_hosts