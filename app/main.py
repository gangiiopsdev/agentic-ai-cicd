from fastapi import FastAPI
import subprocess
from typing import Optional
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> dict:
    try:
        # Validate input to prevent command injection
        if not host.strip().isalnum() or len(host) > 255:
            raise ValueError("Invalid host name")
        subprocess.run(['ping', re.escape(host)], check=True, shell=False)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}