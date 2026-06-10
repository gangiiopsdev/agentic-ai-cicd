from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

# Regex pattern to validate IP address format
IP_PATTERN = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

def ping(host: str):
    if not IP_PATTERN.match(host):
        raise ValueError("Invalid host")
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)