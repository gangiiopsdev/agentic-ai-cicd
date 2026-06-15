from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(hostname: str) -> bool:
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', hostname)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    subprocess.run(shlex.split(f"ping {host}"), check=True)
    return {"status": "completed"}