from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)