from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    result = safe_ping(host)
    return {"status": "completed", "output": result}

import re
def validate_host(host):
    # Simple regex to allow only alphanumeric characters and hyphens
    pattern = r'^[a-zA-Z0-9-]+$'
    return re.match(pattern, host) is not None