from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allowed hosts list)
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {"status": "completed"}