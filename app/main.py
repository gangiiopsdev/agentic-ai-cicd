from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if re.match(r'[a-zA-Z0-9.-_]', e))

def safe_ping(host: str):
    if not host.strip():
        raise ValueError("Invalid host")
    command = ['ping', *shlex.split(sanitize_input(host))]
    subprocess.run(command, check=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}