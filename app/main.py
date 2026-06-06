from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    # Enhanced validation: allow only alphanumeric characters and some common delimiters
    return bool(re.match(r'^[a-zA-Z0-9.-_]+$', host))

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        command = f'ping {host}'
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'reason': 'Invalid host input'}, 400