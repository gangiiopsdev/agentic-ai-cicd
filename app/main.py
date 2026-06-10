from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid hostname"
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)