from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = ['example.com', 'test.example.com']
def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host) or len(host) > 255:
        return False
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', f'/bin/ping {host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}