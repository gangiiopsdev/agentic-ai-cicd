from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError("Host cannot be empty")
    command = ['ping'] + shlex.split(host)
    subprocess.call(command)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)