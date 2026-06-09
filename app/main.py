from fastapi import FastAPI
import subprocess
import shlex
import re

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input further if necessary
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or 'ping' in host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}