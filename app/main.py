from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError('Invalid hostname provided')
    command = ['ping', shlex.quote(host)]  # Use shlex.quote for safe argument passing
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}