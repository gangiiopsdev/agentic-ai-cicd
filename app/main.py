from fastapi import FastAPI
import subprocess
import re
import shlex

git_path = 'git'  # Ensure git_path is defined and sanitized

app = FastAPI()

def validate_host(host):
    # Simple regex to allow alphanumeric characters and some special characters
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = shlex.split(f'{git_path} {host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}