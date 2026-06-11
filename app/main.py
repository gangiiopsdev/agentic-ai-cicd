from fastapi import FastAPI
import subprocess
from shlex import quote
def escape_host(host: str):
    return quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', *escaped_host.split()]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}