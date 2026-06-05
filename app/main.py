from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Basic validation to ensure the host is a valid IP or hostname
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))

def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}

    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app.get('/ping')(ping)