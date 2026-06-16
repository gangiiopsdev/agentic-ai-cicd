from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(host: str, credentials: HTTPBasicCredentials = Depends(security)):
    if not host or not host.strip():
        return {"status": "error", "output": "Invalid input"}
    try:
        # Use a whitelist of allowed hosts
        allowed_hosts = ['example.com', 'test.com']
        if host not in allowed_hosts:
            return {"status": "error", "output": "Host not allowed"}
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}