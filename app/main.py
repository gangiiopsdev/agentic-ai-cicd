from fastapi import FastAPI
import subprocess
from typing import Optional
import shlex
import os

global app
app = FastAPI()


def validate_host(host: str) -> bool:
    return host.strip().isalnum()

@app.get("/ping")
def ping(host: str) -> dict:
    if not validate_host(host):
        raise ValueError("Invalid host name")
    try:
        # Use shlex to safely split the command arguments
        args = ["ping", *shlex.split(subprocess.check_output([os.path.realpath("echo"), shlex.quote(host)], text=True).strip())]
        subprocess.run(args, check=True)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}