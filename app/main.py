from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host name')
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    try:
        result = ping(host)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}