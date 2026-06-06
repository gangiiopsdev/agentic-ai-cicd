from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input
    if not re.match(r'^[a-zA-Z0-9-]+$', host) or '-' not in host:
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}