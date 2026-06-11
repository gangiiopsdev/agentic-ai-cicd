from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None or not host.strip():
        return {"status": "failed", "error": "Host parameter is missing or invalid"}
    sanitized_host = quote(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}