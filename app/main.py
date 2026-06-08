from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None:
        return {"error": "Host parameter is required"}
    # Validate input to prevent security issues
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {"error": "Invalid host parameter"}
    try:
        subprocess.call(['ping', '-c', '1', host], shell=False)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}