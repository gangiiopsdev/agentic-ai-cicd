from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not re.match(r'^[0-9]{3}$', host):
        return {'status': 'error', 'message': 'Invalid host input'}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}