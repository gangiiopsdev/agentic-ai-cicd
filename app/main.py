from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Failed to ping {host}: {e.stderr}"

def safe_ping_path(host: str):
    # Ensure the host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    return host

@app.get="/ping")
def ping(host: str):\n    safe_host = safe_ping_path(host)\n    result = safe_ping(safe_host)\n    return {"status": "completed", "result": result}