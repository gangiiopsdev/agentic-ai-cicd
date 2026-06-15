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
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}