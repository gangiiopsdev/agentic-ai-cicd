from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {"status": "invalid host"}
    command = shlex.split(f'ping {host}')
    subprocess.call(command, shell=False)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)