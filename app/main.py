from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host is a valid IP or hostname
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host], shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)
def validate_host(host: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None