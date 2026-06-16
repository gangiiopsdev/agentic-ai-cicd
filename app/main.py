from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid hostname'
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)