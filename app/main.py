from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    command = ['ping', host]
    subprocess.run(command, shell=False, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(shlex.quote(host))
    return {"status": "completed"}