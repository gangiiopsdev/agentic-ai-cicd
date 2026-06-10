from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_hostname(hostname):
    if not re.match(r'^[a-zA-Z0-9.-]+$', hostname):
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_hostname(host)
        args = shlex.split(f'ping {shlex.quote(sanitized_host)}')
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            return {'error': f'Ping failed: {error.decode()}'}, process.returncode
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400