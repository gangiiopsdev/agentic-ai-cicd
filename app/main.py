from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if host.strip().isnumeric() or '.' in host:
        args = ['ping', '-c', '1', host]
        subprocess.run(args, check=True)
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)