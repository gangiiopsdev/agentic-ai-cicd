from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}