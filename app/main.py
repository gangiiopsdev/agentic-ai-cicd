from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}