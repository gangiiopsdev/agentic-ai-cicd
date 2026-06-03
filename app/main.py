from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True and validation of the host parameter
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str): safe_ping(host) return {"status": "completed"}
def validate_host(host: str) -> bool:
    # Add logic to validate the host parameter
    allowed_hosts = ['example.com', 'localhost']
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        return False
    return host in allowed_hosts