from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced security check
    if not host.isalnum() or '<' in host or '>' in host or '&' in host or ';' in host:
        raise ValueError('Invalid hostname')
    # Validate the host using a regular expression for allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}