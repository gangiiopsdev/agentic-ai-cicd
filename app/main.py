from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host is a valid IP or hostname
    if not validate_host(host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout
global app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)
def validate_host(host: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None