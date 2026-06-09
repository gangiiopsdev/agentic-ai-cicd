from fastapi import FastAPI
import subprocess
from typing import Optional
import shlex
import os

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.strip().isalnum()

def safe_ping(host: str) -> dict:
    if not validate_host(host):
        raise ValueError("Invalid host name")
    try:
        args = ["ping", *shlex.split(shlex.quote(host))]
        subprocess.run(args, check=True)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}

@app.get("/ping")
def ping(host: str) -> dict:
    return safe_ping(host)