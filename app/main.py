from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression to validate the host input
def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return re.match(pattern, host) is not None

def execute_ping(host):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)