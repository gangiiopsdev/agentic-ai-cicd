from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(host):
    return re.sub(r'[^a-zA-Z0-9.-]+', '', host)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}