from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host: str):
    # Basic validation to ensure the host does not contain malicious characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError('Invalid host name')

def execute_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return execute_ping(host)