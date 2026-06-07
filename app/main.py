from fastapi import FastAPI
import subprocess
import shlex
global_hosts = {'example.com'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        subprocess.call(shlex.split(f"ping {host}"))
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}