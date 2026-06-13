from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Regular expression to match allowed characters in hostnames/IP addresses
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host):
        raise ValueError('Invalid input')
    args = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}