from fastapi import FastAPI
import subprocess
import shlex
import re
global app = FastAPI()

def sanitize_input(input_str):
    return ''.join(char for char in input_str if re.match(r'^[-a-zA-Z0-9:.]*$', char))[:64]

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'error': 'Invalid host'}, 400
    command = shlex.split(f'ping -c 1 {sanitized_host}')
    subprocess.run(command, check=True)
    return {'status': 'completed'}