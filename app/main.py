from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def is_valid_host(host):
    return host.replace('.', '').isdigit()
@ping.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    # Use subprocess.run with shell=False and validate input thoroughly
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}