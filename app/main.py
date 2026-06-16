from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)