from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def run_ping(host: str):
    # Validate the input to ensure it does not contain potentially dangerous characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid input'
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

@app.get("/ping")
def ping(host: str):
    return run_ping(host)