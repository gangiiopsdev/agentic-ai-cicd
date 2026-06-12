from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)