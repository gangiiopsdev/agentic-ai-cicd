from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid input"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}