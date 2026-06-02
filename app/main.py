from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def sanitize_host(host: str):
    if not host or len(host) > 255:
        return None
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {"status": "failed", "error": "Invalid host name"}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}