from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> dict:
    try:
        # Validate input to prevent command injection
        if not host.strip().isalnum():
            raise ValueError("Invalid host name")
        subprocess.call(["ping", host], shell=False)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}