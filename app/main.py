from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_host(host):
    # Simple regex to validate the host format
    pattern = r'^([a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400