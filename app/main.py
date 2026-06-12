from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        raise ValueError('Ping command failed')

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for IP address format
    import re
    pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.([0-9]{1,3}\\.){2}[0-9]{1,3}$'
    return re.match(pattern, host) is not None