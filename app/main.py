from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")

    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

    return {"status": "completed"}