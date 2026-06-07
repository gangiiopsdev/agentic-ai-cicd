from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input
        safe_host = subprocess.quote(host)
        subprocess.call(shlex.split(f'ping {safe_host}'))
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}