from fastapi import FastAPI
import subprocess
from shlex import quote
def is_valid_host(host):
    # Add logic to validate the host parameter
    return host.strip().isdigit()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    result = subprocess.run(["ping", quote(host)], capture_output=True, text=True, check=True)
    return {"stdout": result.stdout}