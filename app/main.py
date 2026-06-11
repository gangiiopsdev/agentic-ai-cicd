from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import List
import re

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1', quote(host)], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}