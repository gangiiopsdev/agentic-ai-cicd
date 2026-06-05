from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9._-]+$', host) or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}