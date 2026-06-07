from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError("Invalid host")
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.escape(sanitize_host(host))
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}