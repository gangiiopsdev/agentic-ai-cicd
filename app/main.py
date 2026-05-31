from fastapi import FastAPI
import subprocess
import re
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host) or len(host.split('.')) != 4:
        raise ValueError("Invalid host name")
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}
try:
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
except cimport as e:
    return {"status": "failed", "error": e.stderr}