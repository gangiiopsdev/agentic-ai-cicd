from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Strengthened regex to allow only alphanumeric, hyphen, and dot characters
    if not re.match(r'^[a-zA-Z0-9.-]{1,64}$', host):  # Limiting the length for practical purposes
        raise ValueError("Invalid host")
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}