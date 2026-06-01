from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Validate host input (e.g., allow only certain domains)
    if not re.match(r'^example\.com$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}