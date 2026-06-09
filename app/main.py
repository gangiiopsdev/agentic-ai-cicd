from fastapi import FastAPI
import subprocess
from typing import Optional
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it only contains allowed characters (e.g., alphanumeric and specific symbols)
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {
            "status": "error",
            "message": "Invalid host"
        }

    # Validate the host to ensure it does not contain potentially malicious patterns
    if re.search(r'[<>;{}|&*?`~\]', host, re.IGNORECASE):
        return {
            "status": "error",
            "message": "Invalid host"
        }

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }