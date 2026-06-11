from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with validation and quoting
    if not host.isalnum():
        raise ValueError('Invalid input for ping host')
    command = ['ping', quote(host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return result.stdout.decode()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)