from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return execute_ping(host)

def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None