from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.strip() or len(host) > 255:
        raise ValueError("Invalid host")
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    # Safe implementation using a full command and shell=False
    subprocess.call(['ping', '-c', '1', host], shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {"result": ping(host)}