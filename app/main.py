from fastapi import FastAPI
import subprocess
cimport shlex
import re

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to ensure it does not contain unexpected characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host parameter")
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}