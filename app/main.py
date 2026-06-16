from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        raise ValueError("Invalid host name")
    return host

@app.get="/ping")
def ping(host: str):