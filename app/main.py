from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

    args = shlex.split(f'ping {host}')
    return run_command(args)