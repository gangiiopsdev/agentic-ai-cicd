from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host.strip():
        raise ValueError("Host cannot be empty")
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)