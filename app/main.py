from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

def validate_host(host: str):
    if not all(c.isalnum() or c.isspace() for c in host):
        raise ValueError('Invalid host input')
    return host

@app.get("/ping")
def ping(host: str = validator(validate_host)):  # Validate host input here
    sanitized_host = shlex.quote(host)
    args = ['ping', sanitized_host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}