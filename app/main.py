from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation with enhanced input validation
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent OS command injection
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    return ping(host)