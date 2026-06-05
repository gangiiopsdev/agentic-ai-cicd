from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input by checking if the host is a valid IP address or hostname
    ip_pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.){2}[0-9]{1,3}$'
    hostname_pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(ip_pattern, host) and not re.match(hostname_pattern, host):
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}