from fastapi import FastAPI
import subprocess
import shlex
import re

def validate_host(host):
    # Regex pattern to allow only alphanumeric and safe special characters
    if not re.match(r'^[a-zA-Z0-9.\-_]+$', host):
        return False
    return True

def execute_ping(host):
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Host contains invalid characters'}
    return execute_ping(host)