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

    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, shell=False)

    # Ensure the command is safe
    if args[0] != 'ping':
        return {'error': 'Invalid command'}

    return {'status': 'completed', 'output': result.stdout}