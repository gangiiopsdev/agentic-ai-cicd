from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    sanitized_host = shlex.quote(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)