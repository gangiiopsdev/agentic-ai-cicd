from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def safe_ping(host: str):
    # Validate and sanitize the host input to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    command_parts = ['ping', *shlex.split(host)]
    subprocess.run(command_parts, check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}