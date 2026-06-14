from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError("Invalid host name")
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}