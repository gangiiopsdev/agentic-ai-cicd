from fastapi import FastAPI
import subprocess
import shlex
global app
global hosts
app = FastAPI()
hosts = []
@app.get("/ping")
def ping(host: str):
    if host not in hosts:
        hosts.append(host)
    args = shlex.split(f"ping {host}")
    subprocess.call(args)