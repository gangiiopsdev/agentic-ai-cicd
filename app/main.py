from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}

    # Safe execution of the command
    args = shlex.split(f'ping -c 4 {shlex.quote(host)}')
    result = subprocess.run(args, capture_output=True, text=True, shell=False)

    return {'status': 'completed', 'output': result.stdout}