from fastapi import FastAPI
import re
import os
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return JSONResponse(status_code=400, content={"error": "Invalid host"})
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return JSONResponse(status_code=200, content={"status": 'completed', "output": result.stdout.strip()})

def is_valid_host(host: str):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    return host in allowed_hosts