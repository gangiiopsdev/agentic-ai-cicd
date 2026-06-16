from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression to validate host input
def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host input')
    args = ['ping', host]
    subprocess.run(args, check=True)