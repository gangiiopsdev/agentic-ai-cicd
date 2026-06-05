from fastapi import FastAPI
import subprocess
from shlex import quote
def is_valid_host(host):
    # Add logic to validate the host parameter
    return host.strip().isdigit()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Host parameter is required and must be a valid IP address or hostname")
    escaped_host = quote(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}