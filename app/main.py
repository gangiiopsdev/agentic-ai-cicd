from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)