from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

def is_safe_host(host: str) -> bool:
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example safe hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}