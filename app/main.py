from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid host format"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {"status": "completed"}