from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    # Define a list of allowed hosts or use regex matching
    return host in ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}