from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    # Use subprocess with a whitelist of allowed hosts or use a safer method
    subprocess.run(['ping', '-c', '1', '8.8.8.8'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return {"status": "completed"}