from fastapi import FastAPI
import subprocess
from shlex import quote
def is_valid_host(host):
    # Add logic to validate the host parameter
    return host.strip().isdigit()

app = FastAPI()

@app.get("/ping")
def ping(host: str):