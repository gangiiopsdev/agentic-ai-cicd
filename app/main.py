from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here, e.g., check if the host is within a whitelist
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    command = shlex.split(f'ping -c 1 {host}')
    subprocess.call(command)
    return {"status": "completed"}