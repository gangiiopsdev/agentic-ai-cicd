from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or not host.strip():
        raise ValueError('Host parameter cannot be empty or whitespace only')
    args = shlex.split(f"ping {host}")
    subprocess.call(args, shell=False)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)