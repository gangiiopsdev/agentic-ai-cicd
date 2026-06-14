from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        raise ValueError('Invalid host name')
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)