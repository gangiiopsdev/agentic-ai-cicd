from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def is_valid_host(host):
    # Basic validation of host name
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    subprocess.run(["ping", quote(host)], check=True, capture_output=True)
    return {"status": "completed"}