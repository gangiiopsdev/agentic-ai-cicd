from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

def is_valid_host(host: str) -> bool:
    # Simple regex to validate hostnames/IP addresses
    import re
    return re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) is not None

@app.get("/ping")
def ping_route(host: str):
    return ping(host)