from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not host.strip() or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True, check=False)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}