from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = shlex.split('ping ' + host)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def is_valid_host(host: str) -> bool:
    # Simple regex to validate hostnames/IP addresses
    import re
    return re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) is not None

@app.get("/ping")
def ping_route(host: str):
    return ping(host)