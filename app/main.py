from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    # Validate the input using a regular expression to allow only alphanumeric characters and dots
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return 'Invalid input'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)