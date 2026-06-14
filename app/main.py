from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if host.strip().isnumeric() or '.' in host:
        subprocess.run(shlex.split('ping ' + host), check=True)
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):