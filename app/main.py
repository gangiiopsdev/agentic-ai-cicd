from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        raise ValueError("Invalid host input")
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = safe_ping(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}