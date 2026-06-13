from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def is_valid_host(host):
    # Regular expression to match a valid hostname
    return bool(re.match(r'^[a-zA-Z0-9.-]{1,255}$', host))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True, text=True)
    return {"status": "completed"}